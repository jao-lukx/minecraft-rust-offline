# Minecraft Rust Offline — Horizon

Distribuição não oficial do [Horizon](https://github.com/horizon-rust/horizon) com suporte a
perfis locais sem login Microsoft. Preparada a pedido de **jao-lukx** pelo agente Codex.

## Baixar para jogar no Linux x86_64

Abra a [release offline-v0.1.0](https://github.com/jao-lukx/minecraft-rust-offline/releases/tag/offline-v0.1.0)
e baixe **horizon-offline-linux-x86_64-debug.tar.gz**. Esse pacote contém os executáveis já
compilados, o código-fonte completo e as instruções. Não é necessário instalar Rust para
usar esses executáveis.

O [guia COMO-JOGAR.md](COMO-JOGAR.md) explica as dependências no Arch Linux, a preparação dos
recursos e como iniciar o perfil offline. Os executáveis são builds de desenvolvimento,
não otimizados, para Linux x86_64 com glibc 2.39 ou superior.

Este repositório é o ponto de distribuição e documentação. O snapshot completo do código
alterado está nos assets da release, inclusive no ZIP **horizon-offline-profiles-source.zip**.
Os mesmos pacotes estão na pasta [downloads](downloads/). Os arquivos automáticos “Source code”
do GitHub contêm este repositório de distribuição; para executar, prefira o pacote Linux indicado.

## O que mudou

- Perfis offline podem ser criados e selecionados sem login Microsoft.
- Nomes são persistidos em `accounts.json`; UUIDs seguem `OfflinePlayer:<nome>` do Minecraft.
- A sessão offline é explícita, não fabrica tokens e ignora arquivos de sessão Microsoft herdados.
- CLI, interface e MCP compartilham a passagem do perfil ao cliente.
- O login Microsoft e o requisito de proprietário para downloads da Mojang foram preservados.
- A interface informa que perfis offline não autenticam em servidores que exigem conta original.

Origem: `horizon-rust/horizon`, base `e4472a7`; alteração local `34ead8e`, branch
`feat/offline-profiles`. A licença MIT original está em [LICENSE](LICENSE); os avisos de terceiros
acompanham o código completo nos pacotes.

## Recursos e validação

Você precisa dos arquivos de sua própria cópia de Minecraft: Java Edition **26.3** e do server
jar correspondente. Jars, assets, recursos preparados, mundos, contas e tokens não estão nos
pacotes. Não compartilhe os recursos gerados pelo preparador.

Builds Linux x86_64 e testes de perfis/sessão passaram. **A interface gráfica e o carregamento
de mundos não foram testados**, e não foi possível executar os harnesses que exigem Minecraft.
Esta distribuição não é uma release oficial do Horizon nem um produto oficial da Mojang/Microsoft.
