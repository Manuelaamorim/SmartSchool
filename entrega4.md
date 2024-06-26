# Entrega 04

## Links relevantes:
<ul>
  <li>
    <a  href="https://smartschl.atlassian.net/jira/software/projects/SSC/boards/1"
      >Projeto no Jira</a>
  </li>
    <li>
    <a  href="https://www.figma.com/file/OodUDTbRUE7cAgmlOUiEr9/SmartSchool?type=design&node-id=0-1&mode=design&t=V3uiesp8LFjSo9ET-0"
      >Protótipo de Lo-Fi no Figma</a>
  </li>
  <li>
    <a  href="https://www.youtube.com/watch?v=c7KJYMsQ75s&feature=youtu.be"
      >Screencast do Protótipo Lo-fi - Entrega 04</a>
  </li>
  <li>
    <a  href="https://www.youtube.com/watch?v=mSL1M9w5k4k"
      >Screencast CI/CD com Build e Deployment Automatizado - Entrega 04</a>
  </li>
  <li>
    <a  href="https://www.youtube.com/watch?v=6hpqK0LBPxM"
      >Screencast da Execução dos Testes - Entrega 04</a>
  </li>
   <li>
    <a  href="https://www.canva.com/design/DAGGk8p_AkY/pkSjzKth6wqIWvz8L3Y-jQ/view?utm_content=DAGGk8p_AkY&utm_campaign=designshare&utm_medium=link&utm_source=editor"
      >Apresentação da Entrega 04 no Canva</a>
  </li>
    <li>
    <a  href="https://github.com/Manuelaamorim/SmartSchool/blob/main/contributing.md"
      >Instruções para contribuição no projeto</a>
  </li>
</ul>
<br/>

## Deployment das histórias produzidas:
<ul>
  <li>
    <a  href="https://fdssmartschool.azurewebsites.net/"
      >Projeto na Azure</a>
  </li>
  <li>
    <a  href="https://www.youtube.com/watch?v=EbdvpUNE0RE"
      >Screencast da Azure - Entrega 04</a>
  </li>
</ul>
<br/>

## Instruções de acesso ao projeto:

Na página inicial do nossa aplicação, os usuários podem escolher entre três perfis distintos: Aluno, Funcionário e Professor. Cada um deles redireciona o usuário a página de seu respectivo login.

Para acessar como Aluno, utilize o CPF "60356365433" e a matrícula "ale12345". Com esse login, os usuários podem visualizar informações como dados de saúde, boletim escolar, horários de aula e frequência da estudante Ana Luiza Eugênio. Além disso, há uma opção para que Ana Luiza envie um formulário de contato para a instituição de ensino.

Realizando o logout, o login dos professores deve ser feito utilizando o CPF "03662551004" e a senha "jllm3328". Ao fazer isso, o usuário entrará no menu principal do professor João Lucas Lucena Maranhão. Nesse menu, ele poderá registrar a frequência e as notas dos alunos, além de enviar um formulário de contato para a instituição de ensino.

Após realizar o logout e retornar à página principal, escolha o perfil de "Funcionário" para fazer login. Utilizando o CPF "92873712491" e a matrícula "mlbc9916", o acesso é feito como Marcos Luiz Bonifácio Cordeiro, que possui autorização para cadastrar novos alunos, professores, disciplinas e turmas. Se o cadastro for concluído com sucesso, o usuário será redirecionado para uma página de confirmação.

Para utilizar outros dados cadastrados no Banco de Dados Azure, consulte as informações detalhadas abaixo.

<ul>
  <li>
    <a  href="https://docs.google.com/document/d/1zgVShyUxGV-HEYkiDcIPZz-uAUELK1W01pC6oIA0J6Q/edit"
      >Documento com as Informações do Banco de Dados da Azure</a>
  </li>
</ul>
<br/>

## Diagrama de atividades do sistema:

![Flowchart Template (1)](https://github.com/Manuelaamorim/SmartSchool/assets/142773064/a13124bd-1d96-408d-9cfb-14890b498f8f)


<br/>

## Issues/bug tracker:
  
  - Issues em abertas:

  ![image](https://github.com/Manuelaamorim/SmartSchool/assets/142773064/94eac44d-62f5-41d4-954e-84f6960532f3)
       
  - Issues fechadas:

![image](https://github.com/Manuelaamorim/SmartSchool/assets/142773064/607af412-bd11-442a-a1ea-8106c2cb9a03)
![image](https://github.com/Manuelaamorim/SmartSchool/assets/142773064/78ac8918-ef9f-49ae-a5bb-d5e183dad963)

<br/>

 ## Print do backlog do projeto:
  
![image](https://github.com/Manuelaamorim/SmartSchool/assets/142773064/32adf2b2-9a9c-4bb2-a071-220d6c496999)


<br/>  
 
## Print do quadro da Sprint:

![image](https://github.com/Manuelaamorim/SmartSchool/assets/142419881/e54eb93f-380d-450d-a74a-64fb182d9226)


<br/>

## Relato da Programação em Par experimentada:


*Introdução*

Dando continuidade ao projeto de desenvolvimento da aplicação Smart School, a última etapa demandou a implementação de três novas histórias juntamente com a realização de Testes de Sistema (E2E) Automatizados utilizando a ferramenta Cypress. Nos tópicos seguintes, serão detalhadas as experiências de cada dupla durante esta etapa do projeto.

*Par 01 – Beatriz e Manuela*

O Par 01 concentrou seus esforços na implementação da funcionalidade de cadastro de alunos, aspecto essencial do negócio a que se destina a aplicação. Nessa implementação, os membros colaboraram ativamente e de forma conjunta. Nos testes, alguns cenários foram criados por cada membro de forma separada, com revisão posterior pelo outro integrante. Destaque-se que a atuação conjunta demonstrou ser mais eficaz, pois permitiu a troca contínua de ideias e soluções, resultando em uma aplicação mais confiável.

*Par 02 – Lisa e Luziane*

Por sua vez, o Par 02 assumiu a responsabilidade pelo desenvolvimento do cadastro de disciplinas, outra peça fundamental do negócio. Este par também adotou a técnica de implementação conjunta da funcionalidade e construção de alguns testes em separado, com posterior revisão pelo outro membro. Da mesma forma que o par anterior, o trabalho em conjunto provou ser mais eficiente, pois possibilitou uma troca mais efetiva de ideias e soluções, levando a um código mais robusto e a uma menor incidência de inconsistências.

*Par 03 – Matheus e Ygor*

Por fim, o Par 03 dedicou-se à implementação do cadastro de turmas, que faz a ligação entre alunos, professores e disciplinas, provavelmente uma das funcionalidades mais essenciais do negócio. A parte principal da implementação, assim como a construção dos testes, foi realizada em conjunto, enquanto o estilo visual (CSS) foi desenvolvido separadamente. A eficácia da programação em par, especialmente no que se refere à troca contínua de experiências entre os membros, também restou evidente neste caso, refletindo os mesmos benefícios observados no trabalho do par anterior.

Conclusões

A última etapa do projeto transcorreu de forma positiva, com cada equipe seguindo adiante com suas tarefas de forma consistente. Destaque-se que, em alguns momentos, em virtude dos prazos apertados para a entrega de algumas atividades, os integrantes das duplas atuaram de forma independente em um ou outro aspecto das suas histórias. Apesar de agilizar a entrega da funcionalidade, essa atuação não se mostrou tão proveitosa quanto a programação em par, a qual foi retomada tão logo quando foram percebidos os aspectos negativos de sua ausência: falta de comunicação entre os integrantes, implementação de aspectos aparentemente contraditórios, dentre outros. Ao final deste trabalho, é unânime entre os membros da equipe a importância desta técnica e é certo afirmar que esta experiência fortalecerá a capacidade de seus membros desenvolverem futuros projetos.
