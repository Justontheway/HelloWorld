/*
 * src/db/mysql/main.c
 *
 * NOTHING @ justontheway.com
 *
 */

#include <stdio.h>

#define LOG_ERROR1(fmt, arg...)  printf("\033[31m[ ERROR ] " fmt "\033[0m\n", ##arg);
#define LOG_ERROR2(fmt, args...) printf("\033[31m[ ERROR ] " fmt "\033[0m\n", ##args);
#define LOG_ERROR3(fmt, ...)     printf("\033[31m[ ERROR ] " fmt "\033[0m\n", __VA_ARGS__);
#define LOG_ERROR4(fmt, ...)     printf("\033[31m[ ERROR ] " fmt "\033[0m\n", ##__VA_ARGS__);

int main(int argc, const char *argv[])
{
    LOG_ERROR1("test1 line %d", __LINE__);
    LOG_ERROR2("test2 line %d", __LINE__);
    LOG_ERROR3("test3 line %d", __LINE__);
    LOG_ERROR4("test4 line %d", __LINE__);
    return 0;
}
