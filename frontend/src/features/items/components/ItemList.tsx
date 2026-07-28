import React from 'react';
import { useItems, useDeleteItem } from '../hooks/useItems';

export const ItemList: React.FC = () => {
  const { data: items, isLoading, isError, error } = useItems();
  const deleteItemMutation = useDeleteItem();

  const handleDelete = (id: string, nombre: string) => {
    if (confirm(`¿Estás seguro de que deseas eliminar el ítem "${nombre}"?`)) {
      deleteItemMutation.mutate(id);
    }
  };

  if (isLoading) return <div>Cargando catálogo de ítems desde el servidor...</div>;
  if (isError) return <div style={{ color: 'red' }}>Error al cargar ítems: {(error as Error).message}</div>;

  return (
    <div style={{ marginTop: '20px' }}>
      <h3>Catálogo de Ítems Disponibles</h3>
      {items && items.length === 0 ? (
        <p>No hay ítems registrados en la base de datos.</p>
      ) : (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {items?.map((item) => (
            <li
              key={item.id}
              style={{
                border: '1px solid #ddd',
                padding: '10px',
                marginBottom: '10px',
                borderRadius: '5px',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
              }}
            >
              <div>
                <strong>{item.nombre}</strong> ({item.categoria}) - <small>ID: {item.id}</small>
                <p style={{ margin: '5px 0', fontSize: '0.9em', color: '#666' }}>
                  {item.descripcion || 'Sin descripción'}
                </p>
                <small>
                  Stack Máx: {item.stack_maximo} | Compra: ${item.precio_compra} | Venta: ${item.precio_venta}
                </small>
              </div>

              <button
                onClick={() => handleDelete(item.id, item.nombre)}
                disabled={deleteItemMutation.isPending}
                style={{
                  backgroundColor: '#ff4d4f',
                  color: 'white',
                  border: 'none',
                  padding: '6px 12px',
                  borderRadius: '4px',
                  cursor: 'pointer',
                }}
              >
                Eliminar
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};