/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: geymat <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/23 16:55:05 by geymat            #+#    #+#             */
/*   Updated: 2023/11/29 18:57:27 by geymat           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

static void	*join_and_strlcpy(char buffer[BUFFER_SIZE], char *res)
{
	res = ft_strjoin_free_first(res, buffer, ft_endline(buffer));
	if (!res)
		return (NULL);
	ft_strlcpy(buffer, buffer + ft_endline(buffer),
		BUFFER_SIZE - ft_endline(buffer) + 1);
	return (res);
}

static int	read_return(char *buffer, ssize_t *nb, int fd)
{
	*nb = read(fd, buffer, BUFFER_SIZE);
	if (*nb <= 0)
		return (0);
	buffer[*nb] = 0;
	return (1);
}

static void	fill_the_string(char *buffer, int fd, char **res, ssize_t *nb)
{
	if (!ft_endline(buffer))
	{
		*nb = read(fd, buffer, BUFFER_SIZE);
		if (!*nb)
			return ;
		if (*nb == -1)
			return ;
		buffer[*nb] = 0;
	}
	*res = join_and_strlcpy(buffer, *res);
}

char	*get_next_line(int fd)
{
	ssize_t		nb;
	static char	buffer[1024][BUFFER_SIZE + 1];
	char		*res;

	nb = 1;
	if (BUFFER_SIZE <= 0
		|| (!buffer[fd][0] && !read_return(buffer[fd], &nb, fd)))
		return (NULL);
	res = malloc(1);
	if (!res)
		return (NULL);
	res[0] = 0;
	res = join_and_strlcpy(buffer[fd], res);
	while (res && !ft_endswith(res))
	{
		fill_the_string(buffer[fd], fd, &res, &nb);
		if (nb < 0)
			return (free_ret_null(res));
		if (!nb)
			return (res);
	}
	return (res);
}
