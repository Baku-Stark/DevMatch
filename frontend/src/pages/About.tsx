import { useDocumentTitle } from '../hooks/useDocumentTitle';

export default function About() {
  useDocumentTitle('About Us');

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Sobre Nós</h1>
      <p>Esta é a página About. Aqui você pode falar sobre sua missão, equipe ou história.</p>
    </div>
  );
}