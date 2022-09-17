Select COUNTRY.Continent, ROUND(AVG(CITY.Population),0) as avg_pop
FROM COUNTRY
JOIN CITY
ON COUNTRY.Code = CITY.CountryCode
GROUP BY COUNTRY.Continent
ORDER BY avg_pop ASC;
