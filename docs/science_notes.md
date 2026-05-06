# Science Notes, Assumptions, and Caveats

## What is scientifically robust now
- WCS-aware reprojection and exposure-weighted stacking logic.
- Explicit masking + central galaxy protection strategy.
- Explicit PSF homogenization formula and approximate variance propagation.
- Transparent unit conversion chain (GALEX cps to mJy; nanomaggies to mJy).

## Remaining approximations
1. **Noise model completeness:** Exposure-only GALEX uncertainty is a proxy when full variance maps are unavailable.
2. **PSF kernel shape:** Gaussian kernels approximate true PSFs; mission PSF wings may require empirical kernels.
3. **Mask classification:** Morphology-only contaminant classification can be improved by external catalog cross-match and color priors.
4. **Covariance neglect:** Resampling and convolution create correlated noise not fully represented in per-pixel diagonal variance.

## Recommended publication-grade extensions
- Empirical PSF kernels from stars per field and per band.
- Forced-photometry style masking validation with external star catalogs (e.g., Gaia).
- Monte-Carlo uncertainty propagation through reprojection+convolution.
- End-to-end aperture-based closure tests on calibration fields.
# Science_notes

See README for commands. This document details science_notes for UGC 9024 and NGC 6902 workflows.
