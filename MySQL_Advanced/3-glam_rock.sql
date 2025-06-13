-- Lists all bands with Glam Rock as their main style, ranked by their longevity
SELECT
    band_name,
    CASE
        WHEN split IS NULL OR split = 0 THEN YEAR(CURDATE()) - YEAR(formed)
        ELSE YEAR(split) - YEAR(formed)
    END AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC