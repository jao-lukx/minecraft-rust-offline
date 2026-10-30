# Mods na pasta — launcher offline 0.2.1-offline.1

[Baixar atualização do launcher para Linux x86_64](https://raw.githubusercontent.com/jao-lukx/minecraft-rust-offline/main/downloads/horizon-offline-dropin-launcher-linux-x86_64.tar.gz).

1. Feche o jogo e o launcher. Extraia o pacote e copie seu conteúdo para a pasta do seu `horizon-launcher`, substituindo o launcher. Mantenha `native-source` e `native-tools` ao lado dele.
2. Crie a pasta `mods` ao lado do launcher. Baixe os arquivos `.hnmod` dos mods abaixo e coloque-os nela, sem descompactar.
3. Abra `./horizon-launcher` e clique em **Jogar**. A primeira combinação nova é compilada automaticamente; as próximas aberturas usam o executável guardado. O launcher mostra o progresso e os erros.

- [Mouse Tweaks](https://github.com/jao-lukx/minecraft-rust-mouse-tweaks)
- [Zoom](https://github.com/jao-lukx/minecraft-rust-zoom)
- [JEI](https://github.com/jao-lukx/minecraft-rust-jei)
- [Sodium-inspired](https://github.com/jao-lukx/minecraft-rust-sodium)

Também são aceitas as pastas `mods` e `horizon-native-mods` da instância. Desligue um mod em **Opções → Mods** sem recompilar. Remover/atualizar arquivos escolhe outra compilação; recolocar uma combinação anterior reutiliza seu cache. Remover todos inicia a versão base. Os mundos e perfis continuam na instância original; mantenha as variáveis HORIZON_HOME/HORIZON_LAUNCHER_HOME que já usa.

O launcher traz o aplicador de mods e o snapshot offline com a API de ganchos 4. Baixa Rust automaticamente quando uma combinação ainda precisa compilar. Combinações novas precisam de internet e ferramentas de desenvolvimento do sistema; no Arch Linux, `sudo pacman -S --needed base-devel pkgconf alsa-lib systemd-libs`. Os drivers gráficos e recursos preparados da sua própria cópia de Minecraft Java 26.3 continuam necessários. Requer glibc 2.39 ou mais recente. O launcher desta distribuição não se substitui automaticamente por um launcher upstream sem esses ganchos.

Arquivos `.hnmod` contêm código nativo Rust: não são JARs Java nem plugins binários universais. O launcher guarda o executável gerado por combinação. Este download público contém o launcher e os fontes, não um cliente pré-compilado para todas as combinações.

## Fontes e validação

[Snapshot do código completo](https://raw.githubusercontent.com/jao-lukx/minecraft-rust-offline/main/downloads/horizon-offline-dropin-source.zip). Preserva os perfis offline, acrescenta ganchos de inventário/upload/oclusão e integra a descoberta de mods à ação Jogar. O cache identifica o snapshot offline, as ferramentas, perfil e todos os bytes dos mods.

Builds do launcher e do cliente com o conjunto local passaram. 16 testes de descoberta/pipeline e um teste de compilação automática com dois mods num jogo-fixture passaram, incluindo cache, remoção, atualização e preservação do marcador de mundo. O caminho de instalação de um cliente real pré-compilado também foi testado. Não houve teste visual de uma partida, multiplayer ou benchmark de FPS. Nenhum recurso, jar, conta ou mundo do Minecraft está nos pacotes. Licenças acompanham o código.
