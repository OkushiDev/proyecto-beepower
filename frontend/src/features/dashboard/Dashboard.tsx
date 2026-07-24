import React from 'react';
import { useAuthStore } from '../../store/useAuthStore';
import { useNavigate } from 'react-router-dom';
import { ItemList } from '../items/components/ItemList';
import { ItemForm } from '../items/components/ItemForm';

export const Dashboard: React.FC = () => {
  const logout = useAuthStore((state) => state.logout);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div style={{ padding: '40px', textAlign: 'center' }}>
      <h1>¡Bienvenido a BeePower!</h1>
      <p>Has iniciado sesión correctamente en el sistema.</p>
      <button onClick={handleLogout} style={{ padding: '10px 20px', marginTop: '20px' }}>
        Cerrar Sesión
      </button>

      <h1>Panel de Control - Beepower</h1>

      <ItemForm/>
      <hr />
      {/* Renderizado del catálogo de ítems */}
      <ItemList />
    </div>
  );
};