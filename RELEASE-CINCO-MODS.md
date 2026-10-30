# Minecraft Rust Offline — inclui 5 mods

Pacote para **Linux x86_64** com launcher atualizado, **cinco mods `.hnmod`** e o **cliente já compilado com os cinco juntos**:

- **Mouse Tweaks:** arrastar, coletar e transferir itens com Shift e a roda.
- **Zoom:** segure **C** e ajuste a ampliação com a roda.
- **JEI:** painel de itens; **R** mostra receitas e **U** mostra usos.
- **Sodium-inspired:** uploads adaptativos de chunks e oclusão do Horizon. É uma implementação inicial, não um port do renderizador Sodium original; nenhum ganho de FPS foi medido.
- **Full Bright:** iluminação visual máxima; **B** liga/desliga, sem alterar a luz ou as regras do mundo.

## Baixar e instalar

Baixe **horizon-offline-cinco-mods-linux-x86_64.tar.gz** nos arquivos desta release. O arquivo `SHA256SUMS-CINCO-MODS` permite conferir o download.

1. Feche o jogo e o launcher.
2. Extraia o pacote e copie seu conteúdo para a pasta do seu launcher atual, substituindo `horizon-launcher`.
3. Mantenha `mods`, `native-source`, `native-tools` e `native-prebuilt` ao lado dele. Abra `./horizon-launcher` e clique em **Jogar**.

Os cinco arquivos já estão em `mods/`. Essa combinação usa o cliente pré-compilado. Combinações novas são compiladas automaticamente na primeira execução e ficam em cache. Mundos e perfis continuam na mesma instância; preserve HORIZON_HOME/HORIZON_LAUNCHER_HOME caso já os use.

Requer os recursos já preparados da sua própria cópia de **Minecraft Java 26.3**, os drivers/dependências da instalação anterior e **glibc 2.39 ou mais recente**. O pacote não contém recursos da Mojang, contas ou mundos. Não é uma instalação Java/Fabric/Forge.

## Validação

Builds do launcher e do cliente, testes de controles e testes de compilação automática/cache passaram. O cliente real pré-compilado foi instalado e reutilizado sem baixar compilador. **Partida visual, multiplayer e FPS não foram testados**, por isso esta versão é publicada como pré-release.
