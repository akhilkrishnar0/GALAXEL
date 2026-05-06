# Troubleshooting

## Name resolution failures
- SIMBAD may timeout or object aliases may differ. Use coordinate-filled input table as fallback.

## Missing remote data
- GALEX or DECaLS services may intermittently fail.
- Re-run with retries and preserve downloaded cache in `outputs/*/raw`.

## Unexpected masking
- Tune `masking.nsigma`, `npixels`, and `protect_radius_arcsec`.
- Inspect segmentation overlays in `figures/`.

## Photometric mismatch
- Check PSF target and verify flux-conservation diagnostics before trusting resolved SEDs.
- Ensure consistent units in all input maps.

## Test failures
- Install test extras with `pip install -e .[test]`.
- Ensure `pytest` discovers `src` via project pytest config.
