import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import {
  getItemsRequest,
  createItemRequest,
  deleteItemRequest,
  updateItemRequest,
} from '../api/itemService';
import type { GameItemCreate } from '../types';

export const useItems = () => {
  return useQuery({
    queryKey: ['items'],
    queryFn: getItemsRequest,
  });
};

export const useCreateItem = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: createItemRequest,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['items'] });
    },
  });
};

// Hook para eliminar un ítem
export const useDeleteItem = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: deleteItemRequest,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['items'] });
    },
  });
};

// Hook para actualizar un ítem
export const useUpdateItem = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: updateItemRequest,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['items'] });
    },
  });
};