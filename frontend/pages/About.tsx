import { Helmet } from 'react-helmet';

export default function About() {
  return (
    <>
      <Helmet>
        <title>DevMatch - About</title>
      </Helmet>
      
      <div style={{ padding: '2rem' }}>
        <h1>Sobre Nós</h1>
        <p>Bem-vindo à página About! Aqui você pode falar sobre sua empresa, missão ou equipe.</p>
      </div>
    </>
  );
}
