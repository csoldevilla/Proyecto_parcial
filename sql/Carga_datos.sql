use Kaggle
-- en caso no exista la tabla netflix
if not exists (select  * from sys.tables where object_id = object_id(N'dbo.netflix') and TYPE='U')   
 --drop table netflix
create table netflix (
[show_id] varchar(max),
[type_show] varchar(max),
[title] varchar(max),
[director] varchar(max),
[cast_show] varchar(max),
[country] varchar(max),
[date_added] varchar(max),
[release_year] varchar(max),
[rating] varchar(max),
[duration] varchar(max),
[listed_in] varchar(max),
[description] varchar(max)
)
-- si la tabl aya existe entonces la trunco
TRUNCATE TABLE dbo.netflix

-- ingresar dataset
BULK INSERT dbo.netflix
from 'C:\Users\Christhian\Documents\Cursos\DATA_ANALYTICS_CERTUS\3_20241763DATAOPSMA\proyecto_parcial\python\dataset\netflix_titles.csv'
with
(
FIRSTROW = 2,			-- empieza en la 2da fila, ya que la primera fila son rotulos
FIELDTERMINATOR =',',	-- indicamos el separador de columnas(delimitador),
ROWTERMINATOR ='0x0a'	-- hace referencia a un salto de linea
)
Go

--select  * from netflix
