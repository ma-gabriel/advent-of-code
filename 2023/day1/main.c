/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: geymat <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/01 16:34:39 by geymat            #+#    #+#             */
/*   Updated: 2023/12/01 16:53:01 by geymat           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <stdio.h>
#include <fcntl.h>
#include "get_next_line_bonus.h"
#include <string.h>
#include <ctype.h>


int tkt(char *buff)
{
	buff--;
	while (*++buff)
	{
                if (!strncmp(buff, "one", 3))
                        return (1);
                if (!strncmp(buff, "two", 3))
                        return (2);
                if (!strncmp(buff, "three", 5))
                        return (3);
                if (!strncmp(buff, "four", 4))
                        return (4);
                if (!strncmp(buff, "five", 4))
                        return (5);
                if (!strncmp(buff, "six", 3))
                        return (6);
                if (!strncmp(buff, "seven", 5))
                        return (7);
                if (!strncmp(buff, "eight", 5))
                        return (8);
                if (!strncmp(buff, "nine", 4))
                        return (9);


		if (isdigit(*buff))
			return ( *buff - '0');
	}
	return 0;
}

int tkt2(char *buff)
{
	int i = strlen(buff);
        while (buff[--i])
	{
		if (!strncmp(buff + i, "one", 3))
			return (1);
		if (!strncmp(buff + i, "two", 3))
                        return (2);
		if (!strncmp(buff + i, "three", 5))
                        return (3);
		if (!strncmp(buff + i, "four", 4))
                        return (4);
		if (!strncmp(buff + i, "five", 4))
                        return (5);
		if (!strncmp(buff + i, "six", 3))
                        return (6);
                if (!strncmp(buff + i, "seven", 5))
                        return (7);
                if (!strncmp(buff + i, "eight", 5))
                        return (8);
                if (!strncmp(buff + i, "nine", 4))
                        return (9);


                if (isdigit(buff[i]))
                        return ( buff[i] - '0');
	}
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
