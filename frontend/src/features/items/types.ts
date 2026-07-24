import { number } from "zod";

// Esquema Base/Response de Pydantic
export interface GameItem {
  id: number;
  nombre: string;
  descripcion: string | null;
  categoria: string;
  raro: boolean;
  stack_maximo: number;
  propiedades: Record<string, unknown>; // Mapeo de la columna flexible JSONB
}

// Esquema Create de Pydantic
export interface GameItemCreate {
  id: string;
  nombre: string;
  descripcion?: string;
  icon_path: string;
  categoria: string;
  raro?: boolean;
  stack_maximo?: number;
  precio_compra: number,
  precio_venta: number,
  propiedades?: Record<string, unknown>;
}