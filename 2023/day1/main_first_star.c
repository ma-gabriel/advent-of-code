#include <stdio.h>
#include <fcntl.h>
#include "get_next_line_bonus.h"
#include <string.h>
#include <ctype.h>


int tkt(char *buff)
{
	buff--;
	while (*++buff)
		if (isdigit(*buff))
			return ( *buff - '0');
	return 0;
}

int tkt2(char *buff)
{
	int i = strlen(buff);
        while (buff[--i])
                if (isdigit(buff[i]))
                        return ( buff[i] - '0');
        return 0;
}


int main()
{
	int fd = open("temp.txt", O_RDONLY);
	char *temp = get_next_line(fd);
	int left;
	int right;
	int res;
	res = 0;
	while (temp)
	{
		left = tkt(temp);
		right = tkt2(temp);
		res += left * 10 + right;
		free(temp);
		temp = get_next_line(fd);
	}
	printf("%i\n", res);	
}

