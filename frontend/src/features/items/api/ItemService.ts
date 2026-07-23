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