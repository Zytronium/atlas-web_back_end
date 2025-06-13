-- Lists all bands with Glam Rock as their main style, ranked by their longevity
SELECT
    band_name,
    IFNULL(split, YEAR(CURDATE()) - 1) - formed AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC