/*
For Oracle
*/

SELECT RPAD('*', (21-LEVEL)*2, ' *')
FROM DUAL CONNECT BY LEVEL <= 20;
