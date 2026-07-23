import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { getItemsRequest, createItemRequest } from '../api/itemService';
import type { GameItemCreate } from '../types';

// Hook para consultar el catálogo de ítems
export const useItems = () => {
  return useQuery({
    queryKey: ['items'],
    queryFn: getItemsRequest,
  });
};

// Hook para crear un nuevo ítem e invalidar la caché
export const useCreateItem = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: createItemRequest,
    onSuccess: () => {
      // Obliga a React Query a volver a pedir los ítems al servidor automáticamente
      queryClient.invalidateQueries({ queryKey: ['items'] });
    },
  });
};