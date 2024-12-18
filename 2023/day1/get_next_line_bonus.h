/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.h                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: geymat <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/23 16:54:04 by geymat            #+#    #+#             */
/*   Updated: 2023/11/25 23:58:15 by geymat           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_BONUS_H
# define GET_NEXT_LINE_BONUS_H

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 100
# endif

# include <stdlib.h>
# include <unistd.h>

char	*get_next_line(int fd);
int		ft_endswith(char *test);
size_t	ft_endline(char *s);
char	*ft_strjoin_free_first(char *s1, char *s2, size_t lim);
size_t	ft_strlcpy(char *dst, const char *src, size_t size);
void	*free_ret_null(void *p);

#endif
