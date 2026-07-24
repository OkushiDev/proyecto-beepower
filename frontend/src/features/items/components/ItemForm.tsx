import React, { useState } from 'react';
import { useCreateItem } from '../hooks/useItems';

export const ItemForm: React.FC = () => {
  const createItemMutation = useCreateItem();

  const [formData, setFormData] = useState({
    id: '',
    nombre: '',
    categoria: 'Equipamiento',
    descripcion: '',
    icon_path: 'assets/icons/default.png',
    stack_maximo: 1,
    precio_compra: 0,
    precio_venta: 0,
    propiedadesJson: '{"rarity": "common"}',
  });

  const [error, setError] = useState<string | null>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    try {
      const parsedPropiedades = JSON.parse(formData.propiedadesJson);

      createItemMutation.mutate(
        {
          id: formData.id,
          nombre: formData.nombre,
          categoria: formData.categoria,
          descripcion: formData.descripcion,
          icon_path: formData.icon_path,
          stack_maximo: Number(formData.stack_maximo),
          precio_compra: Number(formData.precio_compra),
          precio_venta: Number(formData.precio_venta),
          propiedades: parsedPropiedades,
        },
        {
          onSuccess: () => {
            setFormData({
              id: '',
              nombre: '',
              categoria: 'Equipamiento',
              descripcion: '',
              icon_path: 'assets/icons/default.png',
              stack_maximo: 1,
              precio_compra: 0,
              precio_venta: 0,
              propiedadesJson: '{"rarity": "common"}',
            });
          },
          onError: (err) => {
            setError('Error al crear el ítem. Verifica que el ID no esté duplicado.');
          },
        }
      );
    } catch (err) {
      setError('El campo Propiedades debe ser un JSON válido.');
    }
  };

  return (
    <div style={{ marginBottom: '2rem', padding: '1rem', border: '1px solid #ccc' }}>
      <h3>Registrar Nuevo Ítem</h3>
      {error && <p style={{ color: 'red' }}>{error}</p>}

      <form onSubmit={handleSubmit}>
        <div>
          <label>ID: </label>
          <input
            type="text"
            value={formData.id}
            onChange={(e) => setFormData({ ...formData, id: e.target.value })}
            required
          />
        </div>

        <div>
          <label>Nombre: </label>
          <input
            type="text"
            value={formData.nombre}
            onChange={(e) => setFormData({ ...formData, nombre: e.target.value })}
            required
          />
        </div>

        <div>
          <label>Categoría: </label>
          <input
            type="text"
            value={formData.categoria}
            onChange={(e) => setFormData({ ...formData, categoria: e.target.value })}
            required
          />
        </div>

        <div>
          <label>Precio Compra: </label>
          <input
            type="number"
            value={formData.precio_compra}
            onChange={(e) => setFormData({ ...formData, precio_compra: Number(e.target.value) })}
          />
        </div>

        <div>
          <label>Precio Venta: </label>
          <input
            type="number"
            value={formData.precio_venta}
            onChange={(e) => setFormData({ ...formData, precio_venta: Number(e.target.value) })}
          />
        </div>

        <div>
          <label>Propiedades (JSON): </label>
          <textarea
            value={formData.propiedadesJson}
            onChange={(e) => setFormData({ ...formData, propiedadesJson: e.target.value })}
          />
        </div>

        <button type="submit" disabled={createItemMutation.isPending}>
          {createItemMutation.isPending ? 'Guardando...' : 'Crear Ítem'}
        </button>
      </form>
    </div>
  );
};