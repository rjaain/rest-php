create table cftv_filemap_config (
Filename varchar(100),
Rcv_Day01 varchar(1),
Rcv_Day02 varchar(1),
Rcv_Day03 varchar(1),
Rcv_Day04 varchar(1),
Rcv_Day05 varchar(1),
Rcv_Day06 varchar(1),
Rcv_Day07 varchar(1),
Rcv_Monthly varchar(1),
Destination_Dir varchar(100),
Red_Data varchar(1),
Data_Start_Row number,
Late_Hours decimal,
Trigger varchar(100),
No_Rows_OK varchar(1),
Rename_To varchar(50),
Concat_To varchar(50),
DOS2UNIX varchar(1),
Custom_Func varchar(50),
Late_Email_Grp varchar(50),
Late_iServ_Grp varchar(50),
Trigger_Grp varchar(50),
Solution_Grp varchar(50),
File_Description varchar(100),
Column_Delim varchar(10),
Max_Row_Tol_Pct decimal,
Max_Col_Tol_Pct decimal,
Max_Size_Tol_Pct decimal,
Compare_By_DOW decimal,
File_ID number);