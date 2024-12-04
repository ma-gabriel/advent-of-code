#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include "get_next_line.h"

int chiant(char *lst, int val)
{
	if (strlen(lst) == val)
		return 1;
	if (lst[val] != '#')
		return (0);
	return 1;
}

int isin(char *lst, char val)
{
	int i;
	i = -1;
	while (lst[++i])
		if (lst[i] == val)
			return i;
	return 10000;
}

int somme(int *arr)
{
	int res;
	int i = -1;
	res = 0;
	while (arr[++i])
		res += arr[i];
	return (res + i);
}

size_t backtracking(char *lst, int *vals, int inter)
{
	size_t res = 0;
	if (!(*vals) && !(isin(lst, '#') - 10000))
		return (!inter);
	if (!(*vals))
		return (0);
	int val = *vals;
	if (!(*lst))
		return (0);
	if (isin(lst, '.') < val)
		printf("1\n");
	else if (!vals[1] && strlen(lst) == val && !(isin(lst, '.') < val))
		return 1;
	else if (!vals[1] && strlen(lst) >= val && !(isin(lst, '.') < val) && !inter && chiant(lst, val) && !(*lst == '#'))
		return backtracking(lst + 1, vals, 0) + (strlen(lst) == val);
	else if (strlen(lst) < somme(vals))
		return res;
	if (*lst != '#')
		res += backtracking(lst + 1, vals, 0);
	if (isin(lst, '.') < val || chiant(lst, val) || inter)
		return res;
	res += backtracking(lst + 1 + val, vals + 1, 0);
	return res;

}

int len_nb(int nb)
{
	if (nb < 10)
		return 1;
	else
		return 2;
}

int main()
{
	int fd = open("valu.txt", O_RDONLY);
	int temp;
	unsigned long res;
	unsigned long temp2;
	char *line;
	char ls[200];
	int vals[50];
	int tata;
	int cinq;
	int nulle = 0;
	int i = 0;

	while (line = get_next_line(fd))
	{
		bzero(ls, 200);
		bzero(vals, 200);
		temp = isin(line, ' ');
		temp2 = res;
		line[temp] = 0;
		strcat(strcat(strcat(strcat(strcat(strcat(strcat(strcat(strcat(ls, line), "?"), line), "?"),line), "?"), line), "?"), line);
		line[temp] = 1;
		line += temp + 1;
		cinq = 5;
		while (cinq)
		{
			while (*line)
			{
				tata = atoi(line);
				vals[i++] = tata;
				line += len_nb(tata) + 1;
				nulle += len_nb(tata) + 1;
			}
			line -= nulle;
			nulle = 0;
			cinq--;
		}
		i = 0;
		res += backtracking(ls, vals, 0);
		printf("%s\n", ls);
		printf("%i, %i, %i, %i, %i, %i, %i, %i, %i, %i, %i, %i, %i, %i, %i, %i,", vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6], vals[7], vals[8], vals[9], vals[10], vals[11], vals[12], vals[13], vals[14], vals[15]);
		printf("%lu\n", res - temp2);
		printf("\n");
		free(line - temp - 1);
	}
	printf("%lu", res);
}
