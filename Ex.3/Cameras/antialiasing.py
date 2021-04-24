Colour Renderer::renderRegion(const Scalar regionX,
                              const Scalar regionY,
                              const Scalar regionSize,
                              const Matrix &transform,
                              const size_t depth) const {
        std::array<Colour, 4> samples;
        Colour supersamples[4];
        Scalar subregion_x[4];
        Scalar subregion_y[4];
        Colour *sample;

        if (debug::RECURSIVE_HIGHLIGHT_DEPTH > 0 &&
            depth == debug::RECURSIVE_HIGHLIGHT_DEPTH) {
                return Colour(debug::RECURSIVE_HIGHLIGHT_COLOUR);
        }

        // Determine the size of a sample.
        const Scalar subregionSize = regionSize / 2;
        // Determine the offset to centre of a sample.
        const Scalar subregionOffset = subregionSize / 2;

        // Iterate over each subregion.
        sample = &samples[0];
        for (size_t index = 0; index < 4; index ++) {
                const size_t i = image::x(index, 2);
                const size_t j = image::y(index, 2);

                // Determine subregion origin.
                const Scalar x = regionX + i * subregionSize;
                const Scalar y = regionY + j * subregionSize;

                // Save X,Y coordinates for later.
                subregion_x[index] = x;
                subregion_y[index] = y;

                // Take a sample at the centre of the subregion.
                *sample++ = renderPoint(x + subregionOffset,
                                        y + subregionOffset,
                                        transform);
        }

        // Determine the average region colour.
        Colour mean;
        mean += samples[0];
        mean += samples[1];
        mean += samples[2];
        mean += samples[3];
        mean /= 4;

        // If we've already recursed as far as we can do, there's
        // nothing more to do.
        if (depth >= maxSubpixelDepth)
                return mean;

        // Iterate over each sub-region.
        for (size_t i = 0; i < 4; i++) {
                sample = &samples[i];

                // Determine the difference between the average region
                // colour and the subregion sample.
                const Scalar diff = mean.diff(*sample);

                // If the difference is above a threshold, recursively
                // supersample this region.
                if (diff > maxSubpixelDiff) {
                        const auto x = subregion_x[i];
                        const auto y = subregion_y[i];

                        // Recursively evaluate sample.
                        *sample = renderRegion(x, y,
                                               regionSize / 4,
                                               transform,
                                               depth + 1);
                }

                // Write updated value.
                supersamples[i] = *sample;
        }

        // Determine mean colour of supersampled subregions.
        Colour output;
        output += supersamples[0];
        output += supersamples[1];
        output += supersamples[2];
        output += supersamples[3];
        output /= 4;

        return output;