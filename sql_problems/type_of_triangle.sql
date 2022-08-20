SELECT \
CASE \
    WHEN A+B>C AND (A=B AND B=C) THEN "Equilateral" \
    WHEN A+B>C AND (((A=B) AND (B!=C))  OR (A!=B) AND (B=C) OR ((A=C) AND (A!=B))) THEN "Isosceles" \
    WHEN A+B>C AND (A!=B AND B!=C AND A!=C) THEN "Scalene" \
    WHEN A+B<C OR A+B=C OR A+C=B THEN "Not A Triangle" \
END \
FROM TRIANGLES;
