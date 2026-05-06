# Configuration Reference

Main parameters (YAML/JSON):
- `output_root`: output base folder.
- `crop_size_arcsec`: common sky cutout size.
- `decals_layer`: Legacy Survey layer name.
- `decals_pixscale`: arcsec/pixel for cutouts.
- `galex_search_radius`: MAST cone radius in degrees.
- `target_psf_fwhm_arcsec`: homogenization target FWHM.
- `grid_cell_size_arcsec`: desired science cell size.
- `random_aperture_count`: validation sampling size.
- `validate_name_coords`: enable SIMBAD-input consistency checks.
- `name_coord_tolerance_arcsec`: consistency threshold.
- `masking.nsigma`, `masking.npixels`, `masking.protect_radius_arcsec`, `masking.compactness_max`, `masking.dilate_pixels`.

Tuning guidance:
- Increase `masking.nsigma` for shallow/noisy fields to reduce false detections.
- Increase `protect_radius_arcsec` for large angular-size galaxies.
- Set `grid_cell_size_arcsec` >= target PSF FWHM for conservative resolved SED analysis.
