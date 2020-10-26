SELECT round(A.LAT_N,4)
FROM (
      SELECT S.LAT_N, @rownum:=@rownum+1 as row_number, @total_rows:=@rownum
      FROM STATION S, (SELECT @rownum:=0) R
      ORDER BY S.LAT_N
     ) as A
WHERE A.row_number IN ( FLOOR((@total_rows+1)/2), FLOOR((@total_rows+2)/2) );