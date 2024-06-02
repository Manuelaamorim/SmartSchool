describe('test cadastrar aluno', () => {
    it('cenario1', () => {
        cy.exec('py manage.py flush --noinput', { failOnNonZeroExit: false });
        cy.exec('py manage.py create_superuser', { failOnNonZeroExit: false });

        cy.visit('/admin'); // http://127.0.0.1:8000/
        cy.get('#id_username').type('admin')
        cy.get('#id_password').type('123456')
        cy.get('.submit-row > input').click()
        cy.wait(1000)
        cy.get('.model-user > :nth-child(2) > .addlink').click()
        cy.get('#id_username').type('34479066420')
        cy.get('#id_password1').type('stellanb123')
        cy.get('#id_password2').type('stellanb123')
        cy.get('.default').click()
        cy.wait(3000)
        cy.get('.model-userfuncionario > td > .addlink')
        cy.get('.model-userfuncionario > td > .addlink').click()
        cy.get('#id_user').select('34479066420');
        cy.get('#id_nome').type('Stella Natalia Bernardes')
        cy.get('#id_matricula').type('stellanb123')
        cy.get('#id_cpf').type('34479066420')
        cy.get('#id_data_de_nascimento').type('11/01/1974')
        cy.get('#id_telefone').type('81982355859')
        cy.get('#id_email').type('stellanb@gmail.com')
        cy.get('.default').click()
        cy.wait(3000)

        cy.get('#logout-form > button').click()

        cy.visit('/');
        cy.get('[href="/funcionario/"] > .botao').click()
        cy.get('#username').type('34479066420')
        cy.get('#password').type('stellanb123')
        cy.get('.btn-submit').click()
        cy.wait(3000)

        cy.get(':nth-child(3) > .nav-menu-texto').click()
        cy.get('#codigo').type('012')
        cy.get('#nome').type('Português')
        cy.get('#carga_horaria').type('60')
        cy.get('#ementa').type('Desenvolver a competência comunicativa dos alunos, aprimorando as habilidades de leitura e escrita')
        cy.get('button').click()
        cy.wait(3000)

        cy.get(':nth-child(3) > .nav-menu-texto').click()
        cy.get('#codigo').type('345')
        cy.get('#nome').type('Matemática')
        cy.get('#carga_horaria').type('60')
        cy.get('#ementa').type('Desenvolver uma base sólida de raciocínio lógico e matemático, utilizando pensamento analítico para resolver problemas')
        cy.get('button').click()
        cy.wait(3000)

        cy.get(':nth-child(3) > .nav-menu-texto').click()
        cy.get('#codigo').type('678')
        cy.get('#nome').type('Ciências')
        cy.get('#carga_horaria').type('60')
        cy.get('#ementa').type('Promover o entendimento dos fenômenos naturais e dos princípios científicos que governam o mundo ao nosso redor')
        cy.get('button').click()
        cy.wait(3000)

        cy.get(':nth-child(3) > .nav-menu-texto').click()
        cy.get('#codigo').type('910')
        cy.get('#nome').type('Artes')
        cy.get('#carga_horaria').type('60')
        cy.get('#ementa').type('Desenvolver a percepção dos alunos nos diversos campos da arte incentivando a apreciação artística')
        cy.get('button').click()
        cy.wait(3000)


        cy.get(':nth-child(4) > .nav-menu-texto').click()
        cy.get('#serie').type('4')
        cy.get('#turma').type('A')
        cy.get('#codigo_materia_1').type('012')
        cy.get('#codigo_materia_2').type('345')
        cy.get('#codigo_materia_3').type('678')
        cy.get('#codigo_materia_4').type('910')
        cy.get('.btn-submit').click()
        cy.wait(300)

        cy.get(':nth-child(1) > .nav-menu-texto').click()
        cy.get('#nome').type('Heitor Alves')
        cy.get('#matricula').type('ha123')
        cy.get('#cpf').type('94674596787')
        cy.get('#data_de_nascimento').type('2015-04-19')
        cy.get('#endereco').type('Rua da Curva, 55 - Casa Forte')
        cy.get('#colegio').type('Maria das Dores')
        cy.get('#serie').type('4')
        cy.get('#turma').type('A')
        cy.get('#nome_responsavel').type('Bruna Alves')
        cy.get('#cpf_responsavel').type('08635421689')
        cy.get('#telefone').type('81988459747')
        cy.get('#email').type('balves@gmail.com')
        cy.get('#peso').type('21.5')
        cy.get('#altura').type('1.25')
        cy.get('#restricao_alimentar').type('Intolerância à lactose')
        cy.get('#tdah').type('Não')
        cy.get('#pcd').type('Não')
        cy.get('.btn-submit').click()
        cy.wait(3000)
    })

    it('cenario2', () => {
        cy.exec('py manage.py flush --noinput', { failOnNonZeroExit: false });
        cy.exec('py manage.py create_superuser', { failOnNonZeroExit: false });

        cy.visit('/admin'); // http://127.0.0.1:8000/
        cy.get('#id_username').type('admin')
        cy.get('#id_password').type('123456')
        cy.get('.submit-row > input').click()
        cy.wait(1000)
        cy.get('.model-user > :nth-child(2) > .addlink').click()
        cy.get('#id_username').type('34479066420')
        cy.get('#id_password1').type('stellanb123')
        cy.get('#id_password2').type('stellanb123')
        cy.get('.default').click()
        cy.wait(3000)
        cy.get('.model-userfuncionario > td > .addlink')
        cy.get('.model-userfuncionario > td > .addlink').click()
        cy.get('#id_user').select('34479066420');
        cy.get('#id_nome').type('Stella Natalia Bernardes')
        cy.get('#id_matricula').type('stellanb123')
        cy.get('#id_cpf').type('34479066420')
        cy.get('#id_data_de_nascimento').type('11/01/1974')
        cy.get('#id_telefone').type('81982355859')
        cy.get('#id_email').type('stellanb@gmail.com')
        cy.get('.default').click()
        cy.wait(3000)

        cy.get('#logout-form > button').click()

        cy.visit('/');
        cy.get('[href="/funcionario/"] > .botao').click()
        cy.get('#username').type('34479066420')
        cy.get('#password').type('stellanb123')
        cy.get('.btn-submit').click()
        cy.wait(3000)

        cy.get(':nth-child(3) > .nav-menu-texto').click()
        cy.get('#codigo').type('012')
        cy.get('#nome').type('Português')
        cy.get('#carga_horaria').type('60')
        cy.get('#ementa').type('Desenvolver a competência comunicativa dos alunos, aprimorando as habilidades de leitura e escrita')
        cy.get('button').click()
        cy.wait(3000)

        cy.get(':nth-child(3) > .nav-menu-texto').click()
        cy.get('#codigo').type('345')
        cy.get('#nome').type('Matemática')
        cy.get('#carga_horaria').type('60')
        cy.get('#ementa').type('Desenvolver uma base sólida de raciocínio lógico e matemático, utilizando pensamento analítico para resolver problemas')
        cy.get('button').click()
        cy.wait(3000)

        cy.get(':nth-child(3) > .nav-menu-texto').click()
        cy.get('#codigo').type('678')
        cy.get('#nome').type('Ciências')
        cy.get('#carga_horaria').type('60')
        cy.get('#ementa').type('Promover o entendimento dos fenômenos naturais e dos princípios científicos que governam o mundo ao nosso redor')
        cy.get('button').click()
        cy.wait(3000)

        cy.get(':nth-child(3) > .nav-menu-texto').click()
        cy.get('#codigo').type('910')
        cy.get('#nome').type('Artes')
        cy.get('#carga_horaria').type('60')
        cy.get('#ementa').type('Desenvolver a percepção dos alunos nos diversos campos da arte incentivando a apreciação artística')
        cy.get('button').click()
        cy.wait(3000)


        cy.get(':nth-child(4) > .nav-menu-texto').click()
        cy.get('#serie').type('4')
        cy.get('#turma').type('A')
        cy.get('#codigo_materia_1').type('012')
        cy.get('#codigo_materia_2').type('345')
        cy.get('#codigo_materia_3').type('678')
        cy.get('#codigo_materia_4').type('910')
        cy.get('.btn-submit').click()
        cy.wait(300)

        cy.get(':nth-child(1) > .nav-menu-texto').click()
        cy.get('#nome').type('Clara Barros')
        cy.get('#matricula').type('cb123')
        cy.get('#cpf').type('29474523579')
        cy.get('#data_de_nascimento').type('2015-03-12')
        cy.get('#endereco').type('Rua da Anta, 105 - Madalena')
        cy.get('#colegio').type('Maria das Dores')
        cy.get('#serie').type('4')
        cy.get('#turma').type('A')
        cy.get('#nome_responsavel').type('André Barros')
        cy.get('#cpf_responsavel').type('09525426439')
        cy.get('#telefone').type('81985489090')
        cy.get('#email').type('abarros@gmail.com')
        cy.get('#peso').type('16.8')
        cy.get('#altura').type('1.19')
        cy.get('#restricao_alimentar').type('Não')
        cy.get('#tdah').type('Não')
        cy.get('#pcd').type('Não')
        cy.get('.btn-submit').click()
        cy.wait(3000)

        cy.get(':nth-child(1) > .nav-menu-texto').click()
        cy.get('#nome').type('Maria Luiza Cavalcanti')
        cy.get('#matricula').type('mlc123')
        cy.get('#cpf').type('29474523579') 
        cy.get('#data_de_nascimento').type('2015-01-30')
        cy.get('#endereco').type('Rua do Paraíso, 126 - Boa Vista')
        cy.get('#colegio').type('Maria das Dores')
        cy.get('#serie').type('4')
        cy.get('#turma').type('A')
        cy.get('#nome_responsavel').type('Aline Cavalcanti')
        cy.get('#cpf_responsavel').type('12702352423')
        cy.get('#telefone').type('81998766364')
        cy.get('#email').type('acavalcanti@gmail.com')
        cy.get('#peso').type('19.8')
        cy.get('#altura').type('1.23')
        cy.get('#restricao_alimentar').type('Não')
        cy.get('#tdah').type('Não')
        cy.get('#pcd').type('Não')
        cy.get('.btn-submit').click()
        cy.wait(3000)
    })
})