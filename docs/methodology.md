# Methodology (Manuscript-Level Technical Notes)

## 1. Scientific objective
This pipeline estimates **resolved UV+optical fluxes** on a common spatial grid for nearby galaxies using:
- **GALEX FUV/NUV** (tracing recent unobscured star formation), and
- **DECaLS g/r/z** (stellar continuum and color structure).

The core requirement is physically consistent, flux-preserving multi-band measurements in matched sky cells.

---

## 2. Target and coordinate handling
Input supports either names, coordinates, or both. If coordinates are missing, the code resolves target names with SIMBAD. If both exist, optional coordinate/name consistency checks are done with an angular tolerance.

### Coordinate consistency
Given input coordinate \(\mathbf{x}_{\rm in}\) and resolved SIMBAD coordinate \(\mathbf{x}_{\rm sim}\), we compute
\[
\Delta\theta = \arccos(\hat{r}_{\rm in}\cdot\hat{r}_{\rm sim})
\]
and flag mismatch when \(\Delta\theta > \Delta\theta_{\rm tol}\).

---

## 3. Data acquisition strategy

### 3.1 GALEX
The MAST query returns all overlapping GALEX observations within a configurable radius. Product tables are filtered to select FITS products associated with intensity/count/exposure/background/weight variants where available. Selection is recorded to provenance files for reproducibility.

### 3.2 DECaLS
DECaLS cutouts are downloaded from Legacy Survey viewer URLs with explicit, configurable layer and pixel scale.

---

## 4. GALEX multi-observation stacking
For each band, overlapping images are reprojected to a common WCS and stacked using exposure weighting.

For pixel \(p\):
\[
I_{\rm stack}(p) = \frac{\sum_i I_i(p)\,E_i(p)}{\sum_i E_i(p)}
\]
where \(I_i\) is intensity (count s\(^{-1}\)) and \(E_i\) is effective exposure (s).

Uncertainty proxy:
\[
\sigma_{\rm stack}(p) \approx \frac{1}{\sqrt{\sum_i E_i(p)}}
\]
This is an approximation when only exposure is available; exact propagation should include product-specific noise models.

Invalid/NaN pixels are excluded from both numerator and denominator.

---

## 5. Contaminant masking (advanced logic)
Masking combines:
1. segmentation detection,
2. morphology-based compactness filtering,
3. central galaxy protection radius,
4. optional dilation.

This design attempts to remove compact foreground/background contaminants while preserving galaxy substructure. We explicitly protect a central zone to avoid eroding bulge/arm complexes.

Current compactness heuristic is based on equivalent radius vs semimajor sigma and eccentricity filtering; this is robust for synthetic/survey-like scenes but should be tuned per dataset depth and PSF.

---

## 6. PSF homogenization
Higher-resolution bands are convolved to a target PSF (default NUV 5.3"). For Gaussian approximation:
\[
\sigma_{\rm ker} = \frac{\sqrt{{\rm FWHM}_{\rm targ}^2 - {\rm FWHM}_{\rm cur}^2}}{2\sqrt{2\ln 2}\;s_{\rm pix}}
\]
where \(s_{\rm pix}\) is pixel scale in arcsec/pixel.

### Error propagation through convolution
If \(V\) is variance image and \(K\) kernel,
\[
V' \approx V * K^2
\]
then \(\sigma' = \sqrt{V'}\).

This neglects covariance between neighboring pixels after interpolation/convolution; limitation is documented.

---

## 7. Reprojection and flux checks
Processed bands are reprojected to a common reference WCS (typically NUV). Flux conservation is evaluated statistically before/after reprojection using integrated flux and per-aperture comparisons.

---

## 8. Cell/grid photometry
A square sky grid is built on the common WCS. For each cell and band:
\[
F_{\rm cell} = \sum_{p\in cell} I(p), \quad
\sigma_{\rm cell} = \sqrt{\sum_{p\in cell} \sigma^2(p)}
\]
with masked pixels excluded.

Cell metadata includes x/y bounds and RA/Dec center.

---

## 9. Unit system

### 9.1 GALEX cps \(\rightarrow\) AB \(\rightarrow\) mJy
Using GALEX zeropoints (FUV=18.82, NUV=20.08):
\[
m_{\rm AB} = -2.5\log_{10}(\mathrm{cps}) + ZP
\]
\[
F_{\rm mJy} = 10^{(16.4 - m_{\rm AB})/2.5}
\]

### 9.2 DECaLS nanomaggies \(\rightarrow\) mJy
\[
1\,\mathrm{nanomaggy} = 3.631\times 10^{-3}\,\mathrm{mJy}
\]

---

## 10. Validation and diagnostics
Recommended QA products:
- mask overlay by band,
- PSF pre/post radial profile checks,
- integrated flux conservation summaries,
- random-cell before/after processing comparisons.

---

## 11. References
- Morrissey et al. 2007, *ApJS*, 173, 682 (GALEX mission/instrument calibration).
- Dey et al. 2019, *AJ*, 157, 168 (Legacy Surveys / DECaLS data products).
- Astropy Collaboration 2022, *ApJ*, 935, 167 (Astropy ecosystem).
- Bradley et al. 2023, `reproject` documentation and package methods.
- Photutils documentation and source extraction API.

