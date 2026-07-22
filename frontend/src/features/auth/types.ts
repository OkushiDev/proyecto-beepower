export interface LoginCredentials {
  username: string; // FastAPI OAuth2PasswordRequestForm espera 'username'
  password: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export interface User {
  id: number;
  username: string;
  email: string;
}