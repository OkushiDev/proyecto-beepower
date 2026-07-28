import { api } from '../../../api/axios';
import type { GameItem, GameItemCreate } from '../types';

// Obtener la lista completa de ítems
export const getItemsRequest = async (): Promise<GameItem[]> => {
  const response = await api.get<GameItem[]>('/items/');
  return response.data;
};

// Crear un nuevo ítem en la base de datos
export const createItemRequest = async (itemData: GameItemCreate): Promise<GameItem> => {
  const response = await api.post<GameItem>('/items/', itemData);
  return response.data;
};

// Eliminar un ítem por su ID
export const deleteItemRequest = async (itemId: string): Promise<void> => {
  await api.delete(`/items/${itemId}`);
};

// Actualizar un ítem existente por su ID
export const updateItemRequest = async ({
  id,
  itemData,
}: {
  id: string;
  itemData: GameItemCreate;
}): Promise<GameItem> => {
  const response = await api.put<GameItem>(`/items/${id}`, itemData);
  return response.data;
};