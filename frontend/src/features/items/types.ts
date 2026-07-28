export interface GameItem {
  id: string; 
  nombre: string;
  descripcion: string | null;
  categoria: string;
  raro?: boolean;
  stack_maximo: number;
  precio_compra: number;
  precio_venta: number;
  propiedades: Record<string, unknown>; // Mapeo de la columna flexible JSONB
}

// Esquema Create de Pydantic / Frontend
export interface GameItemCreate {
  id: string;
  nombre: string;
  descripcion?: string;
  icon_path: string;
  categoria: string;
  raro?: boolean;
  stack_maximo?: number;
  precio_compra: number;
  precio_venta: number;
  propiedades?: Record<string, unknown>;
}