import { z } from 'zod';

export const createItemSchema = z.object({
  id: z.string().min(3, 'El ID debe tener al menos 3 caracteres'),
  nombre: z.string().min(2, 'El nombre es obligatorio'),
  categoria: z.string().min(1, 'La categoría es obligatoria'),
  descripcion: z.string().optional(),
  icon_path: z.string().min(1, 'La ruta del icono es obligatoria'),
  visual_asset_path: z.string().optional(),
  audio_asset_path: z.string().optional(),
  stack_maximo: z.number().int().positive('Debe ser un entero mayor a 0'),
  precio_compra: z.number().int().nonnegative('No puede ser negativo'),
  precio_venta: z.number().int().nonnegative('No puede ser negativo'),
  propiedades: z.record(z.string(),z.unknown()).default({}),
});

export type CreateItemInput = z.infer<typeof createItemSchema>;