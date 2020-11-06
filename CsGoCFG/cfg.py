import os

cfg = """unbindall
// =========== Gameplay ===========
net_graph "1"                                      // Mostrar FPS e outras informações do jogo na tela
net_graphpos "1"                                   // Muda a posição horizontal do net_graph
net_graphheight "64"                               // Muda a posição vertical do net_graph
net_graphproportionalfont "0"                      // Muda o estilo de font do net_graph
net_graphipc "0"                                   // Adiciona novas informações no net_graph
net_graphtext "1"                                  // Ativa os textos do net_graph
cl_autohelp "1"                                    // Desativa a auto ajuda
cl_showhelp "1"                                    // Desativa a auto ajuda
cl_disablefreezecam "0"                            // Desativa a câmera de morte
cl_disablehtmlmotd "0"                             // Remove mensagens do dia ao entrar em um servidor
cl_showfps "0"                                     // Outra opção de mostrar FPS
cl_righthand "1"                                   // Muda a arma para a mão direita ou esquerda
r_drawtracers_firstperson "1"                      // Retirar o flash das armas quando atira
hud_showtargetid "1"                               // Mostra o nome do jogador quando a mira está sobre ele

// =========== Monitor ===========
fps_max_menu "120"                                 // FPS máximo no menu do jogo
fps_max "300"                                      // FPS máximo no jogo
developer "0"                                      // Desativa informações do console de desenvolvedor

// =========== Mira ===========
cl_crosshair_drawoutline "0"
cl_crosshair_dynamic_maxdist_splitratio "0.35"
cl_crosshair_dynamic_splitalpha_innermod "1"
cl_crosshair_dynamic_splitalpha_outermod "0.5"
cl_crosshair_dynamic_splitdist "7"
cl_crosshair_outlinethickness "1"
cl_crosshair_sniper_show_normal_inaccuracy "0"
cl_crosshair_sniper_width "1"
cl_crosshair_t "0"
cl_crosshairalpha "255"
cl_crosshaircolor "5"
cl_crosshaircolor_b "127"
cl_crosshaircolor_g "0"
cl_crosshaircolor_r "255"
cl_crosshairdot "0"
cl_crosshairgap "-3"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairscale "4"
cl_crosshairsize "2"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"
cl_fixedcrosshairgap "-4.5"

// =========== Sons ===========
snd_mixahead "0.025"                               // Deixa o som do CS:GO mais instantâneo

// =========== Mouse ===========
m_mouseaccel2 "0"                                  // Desabilita a aceleração do mouse do Windows por preocupação extra
m_mouseaccel1 "0"                                  // Desabilita a aceleração do mouse do Windows por preocupação extra

// =========== Teclado e mouse ===========
// Configurações de teclado e mouse
option_duck_method "0"                             // Modo de agachar
option_speed_method "0"                            // Modo de andar
sensitivity "4"                                    // Sensibilidade do mouse
zoom_sensitivity_ratio_mouse "1.0"                 // Sensibilidade do zoom
m_rawinput "1"                                     // Dados brutos
m_customaccel "0"                                  // Aceleração do mouse

// Teclas de movimento
bind "i" "show_loadout_toggle"                     // Alternar a exibição do inventário
bind "w" "+forward"                                // Andar para frente
bind "a" "+moveleft"                               // Andar para esquerda
bind "s" "+back"                                   // Andar para trás
bind "d" "+moveright"                              // Andar para direita
bind "SHIFT" "+speed"                              // Andar em silêncio
bind "SPACE" "+jump"                               // Pular
bind "CTRL" "+duck"                                // Agachar

// Teclas de armas
bind "e" "+use"                                    // Usar
bind "MOUSE1" "+attack"                            // Disparar
bind "MOUSE2" "+attack2"                           // Disparo secundário
bind "r" "+reload"                                 // Recarregar
bind "MWHEELUP" "invprev"                          // Selecionar a arma anterior
bind "MWHEELDOWN" "invnext"                        // Selecionar a próxima arma
bind "q" "lastinv"                                 // Última arma usada
bind "g" "drop"                                    // Largar arma
bind "f" "+lookatweapon"                           // Inspecionar arma
bind "b" "buymenu"                                 // Menu de compra
bind "F3" "autobuy"                                // Compra automática
bind "F4" "rebuy"                                  // Comprar anteriores novamente
bind "1" "slot1"                                   // Arma primária
bind "2" "slot2"                                   // Arma secundária
bind "3" "slot3"                                   // Armas corpo a corpo
bind "4" "slot4"                                   // Alternar granada
bind "5" "slot5"                                   // Explosivos e armadilhas
bind "6" "slot6"                                   // Granada explosiva
bind "7" "slot7"                                   // Granada de luz
bind "8" "slot8"                                   // Granada de fumaça
bind "9" "slot9"                                   // Granada de distração
bind "0" "slot10"                                  // Coquetel Molotov
bind "x" "slot12"                                  // Injeção Médica
bind "t" "+spray_menu"                             // Menu de grafites

// Teclas de comunicação
bind "z" "radio"                                   // Mensagem de rádio
bind "u" "messagemode2"                            // Mensagem para equipe
bind "y" "messagemode"                             // Mensagem para todos
bind "v" "+voicerecord"                            // Usar microfone

// Teclas de interface
bind "TAB" "+showscores"                           // Placar
bind "ç" "+cl_show_team_equipment"                 // Exibir equipamento de aliados
bind "m" "teammenu"                                // Escolher equipe

bind "ESCAPE" "cancelselect"

// =========== Controle ===========
// Controle
joystick_force_disabled_set_from_options "1"       // Controle ativado
joy_inverty "0"                                    // Tipo de visão
joy_movement_stick "0"                             // Alavancas de movimento/visão
option_duck_method "0"                             // Modo de agachar
option_speed_method "0"                            // Modo de andar
joy_yawsensitivity "-1"                            // Sensibilidade horizontal
joy_pitchsensitivity "-1"                          // Sensibilidade vertical
zoom_sensitivity_ratio_joystick "1"                // Sensibilidade do zoom

// =========== Configuração de jogo ===========
// Jogo
gameinstructor_enable "0"                          // Ativar mensagens do instrutor do jogo
mm_dedicated_search_maxping "350.000000"           // Ping máx. aceitável na criação de partidas
rate "196608"                                      // Largura de banda máxima aceitável
ui_steam_overlay_notification_position topleft     // Local das notificações da comunidade
con_enable "1"                                     // Ativar console de desenvolvedor (')

// Interface
cl_crosshairstyle "4"                              // Estilo da mira
cl_crosshaircolor "5"                              // Cor da mira
hud_scaling "0.85"                                 // Tamanho da interface
cl_hud_color "0"                                   // Cor da interface
cl_hud_background_alpha "0.5"                      // Opacidade da interface
cl_hud_healthammo_style "0"                        // Estilo dos indicadores de vida/munição
cl_hud_bomb_under_radar "1"                        // Posição do ícone da bomba na interface
cl_hud_playercount_pos "0"                         // Posição do miniplacar
cl_hud_playercount_showcount "0"                   // Estilo do miniplacar
cl_radar_icon_scale_min "0.6"

// Equipe
cl_show_clan_in_death_notice "1"                   // Exibir tags de equipe na lista de mortes
cl_teamid_overhead_always "0"                      // Exibir posição de aliados na interface
cl_teammate_colors_show "1"                        // Exibir cores em aliados no modo Competitivo

// Comunicação
cl_mute_enemy_team "0"                             // Silenciar equipe inimiga
cl_mute_all_but_friends_and_party "0"              // Mute All But Friends
cl_sanitize_player_names "0"                       // Clean Player Names

// Itens
cl_playerspray_auto_apply "1"                      // Grafite rápido (aplicado ao soltar a tecla)
cl_autowepswitch "0"                               // Mudar para arma ao pegá-la
viewmodel_presetpos "1"                            // Posição do modelo de 1° pessoa
cl_showloadout "1"                                 // Sempre exibir inventário
closeonbuy "0"                                     // Fechar menu de compra após uso
cl_use_opens_buy_menu "1"                          // Abrir menu de compra com tecla 'Usar'

// Radar / Tablet
cl_tablet_mapmode "1"                              // Orientação do mapa do tablet
cl_radar_always_centered "1"                       // Jogador centralizado no radar
cl_radar_rotate "1"                                // Rotacionar o radar
cl_hud_radar_scale "1"                             // Tamanho do radar
cl_radar_scale "0.7"                               // Zoom do radar
cl_radar_square_with_scoreboard "1"                // Alternar formato ao abrir placar

// =========== Configurações de áudio ===========
// Áudio
volume "0.2"                                       // Volume geral
snd_musicvolume_multiplier_inoverlay "0"           // Volume da música no painel Steam
voice_caster_scale "1"                             // Volume do narrador da GOTV
snd_surround_speakers "-1"                         // Disposição da saída de áudio
snd_hwcompat "0"                                   // Processamento avançado de áudio 3D
voice_enable "1"                                   // Ativar voz
voice_scale "1"                                    // Volume do VoIP
voice_positional "0"                               // Voz posicional
snd_mute_losefocus "1"                             // Tocar sons quando o jogo estiver em 2° plano

// Música
snd_menumusic_volume "0"                           // Volume do menu principal
snd_roundstart_volume "0"                          // Volume do início da rodada
snd_roundend_volume "0"                            // Volume do fim da rodada
snd_mapobjective_volume "0"                        // Volume de bomba/refém
snd_tensecondwarning_volume "0"                    // Volume do aviso de dez segundos
snd_deathcamera_volume "0.3"                       // Volume da câmera pós-morte
snd_mvp_volume "0"                                 // Volume da música de destaque
snd_dzmusic_volume "0.2"                           // Volume da música da Zona de Perigo

// =========== Configurações de vídeo ===========
// Vídeo
mat_monitorgamma_tv_enabled "0"                    // Modo de cor
mat_monitorgamma "2.2"                             // Brilho
mat_powersavingsmode "0"                           // Economia de energia do laptop

// Bordas da interface
safezonex 1.0                                      // Bordas da interface horizontal
safezoney 1.0                                      // Bordas da interface vertical

// ================ Binds ================
bind "kp_end" "buy vesthelm; buy vest;"
bind "kp_leftarrow" "buy vest;"
bind "kp_home" "buy defuser;"
bind "kp_downarrow" "buy ak47; buy m4a1;"
bind "kp_5" "buy awp;"
bind "kp_pgdn" "buy smokegrenade;"
bind "kp_rightarrow" "buy incgrenade; buy molotov;"
bind "kp_pgup" "buy hegrenade;"
bind "kp_del" "buy flashbang;"
bind "mouse4" "toggle cl_righthand 0 1"

// =========== Launch Options ===========
// -novid -nojoy -d3d9ex +exec forgotten.cfg

playvol buttons\light_power_on_switch_01 0.75      // Efeito de som quando ativa a CFG
host_writeconfig                                   // Salva todas as configurações da CFG

clear
echo "=========================================================================================="
echo "		  _____                           __    __                 			"
echo "		_/ ____\___________  ____   _____/  |__/  |_  ____   ____  			"
echo "		\   __\/  _ \_  __ \/ ___\ /  _ \   __\   __\/ __ \ /    \ 			"
echo "		 |  | (  <_> )  | \/ /_/  >  <_> )  |  |  | \  ___/|   |  \			"
echo "		 |__|  \____/|__|  \___  / \____/|__|  |__|  \___  >___|  /			"
echo "	 	                  /_____/                        \/     \/ 			"
echo "=========================================================================================="
""" 


def findCSFolder():
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" ]
    for letter in letters:
        actual = letter
        print(actual)

        for root, subdirs,files in os.walk(actual+':\\'):
            for d in subdirs:
                if d == "Counter-Strike Global Offensive":
                    path = root +"\\"+ d
                    return path

def findCfgFolder(csPath):
    for root, subdirs,files in os.walk(csPath+"\\"):
            for d in subdirs:
                if d == "cfg":
                    path = root +"\\"+ d
                    return path

def autoexecExists(findCfgFolder):
    path = False
    for root, subdirs,files in os.walk(csPath+"\\"):
            for d in files:
                if d == "autoexec.cfg":
                    path = root +"\\"+ d
                    return path


csPath = findCSFolder()
print(csPath)

findCfgFolder = findCfgFolder(csPath)
print(findCfgFolder)

autoexecPath = autoexecExists(findCfgFolder)
if(autoexecPath == None):
    f = open(findCfgFolder+"\\autoexec.cfg", "w")
    print("Created file")
    print(findCfgFolder+"\\autoexec.cfg")
    open(findCfgFolder+"\\autoexec.cfg",'w').write(cfg)
else:
    print(autoexecPath)
    open(autoexecPath,'w').write(cfg)



