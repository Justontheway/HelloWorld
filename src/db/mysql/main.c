/*
 * src/db/mysql/main.c
 *
 * NOTHING @ justontheway.com
 *
 */

/*
 * mysql_library_init
 * mysql_init
 * mysql_options
 * mysql_real_connect   -   ret ptr
 * mysql_query          -   ret int
 * mysql_store_result   -   ret ptr
 * mysql_num_rows       -   ret unsigned long long
 * mysql_num_fields     -   ret unsigned int
 * mysql_fetch_fields   -   ret ptr
 * mysql_fetch_row      -   ret ptr
 * mysql_close
 * mysql_library_end
 */

#include <stdio.h>
#include <mysql/mysql.h>

#define LOG_ERROR(fmt, ...)       printf("\033[31m[ ERROR ] " fmt "\033[0m", ##__VA_ARGS__);
#define OUTPUT printf

char query_buffer[4096] = {0};

int main(int argc, const char *argv[])
{
    MYSQL conn;
    MYSQL_ROW row;
    MYSQL_RES *queryResult = NULL;
    const char *host = "192.168.116.116";
    const char *user = "nothing";
    const char *passwd = "justontheway";
    const char *dbname = "mysql_test";
    unsigned int port = 3306;
    unsigned int timeout = 20;

    /* init library */
    mysql_library_init(0, NULL, NULL);

    /* init conn */
    mysql_init(&conn);

    /* set options */
    mysql_options(&conn, MYSQL_OPT_CONNECT_TIMEOUT, (const void *)&timeout);
    mysql_options(&conn, MYSQL_OPT_READ_TIMEOUT, (const void *)&timeout);
    mysql_options(&conn, MYSQL_OPT_WRITE_TIMEOUT, (const void *)&timeout);

    do
    {
        /* connect to db */
        if (!mysql_real_connect(&conn, host, user, passwd, dbname, port, NULL, 0))
        {
            LOG_ERROR("fail to connect to db, info : %s\n", mysql_error(&conn));
            break;
        } 

        /* set character set */
        if (mysql_set_character_set(&conn, "utf8"))
        {
            LOG_ERROR("fail to set character-set to utf8, info : %s\n", mysql_error(&conn));
            break;
        }

        /* query */
        sprintf(query_buffer, "select * from dept");
        if (mysql_query(&conn, query_buffer))
        {
            LOG_ERROR("fail to query ***%s***, error : %s\n", query_buffer, mysql_error(&conn));
            break;
        }

        /* store result */
        if (!(queryResult = mysql_store_result(&conn)))
        {
            LOG_ERROR("fail to store result, error : %s\n", mysql_error(&conn));
            break;
        }

        /* get result row-count */
        unsigned long long row_count = mysql_num_rows(queryResult);
        /* get result column-count */
        unsigned int col_count = mysql_num_fields(queryResult);
        OUTPUT("get row %llu, column %u\n", row_count, col_count);

        /* get column name */
        MYSQL_FIELD *field = mysql_fetch_fields(queryResult);
        for (int i = 0; i < col_count; i++)
        {
            OUTPUT("%s    ", field[i].name);
        }
        OUTPUT("\n");

        /* get each column */
        while ((row = mysql_fetch_row(queryResult)))
        {
            for (int i = 0; i < col_count; i++)
            {
                OUTPUT("%s    ", row[i]);
            }
            OUTPUT("\n");
        }

        /* free result */
        mysql_free_result(queryResult);
    } while(0);

    /* close mysql */
    mysql_close(&conn);

    /* fini mysql library */
    mysql_library_end();

    return 0;
}
