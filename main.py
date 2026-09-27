import tcod

from engine import Engine
from input_handler import EventHandler
from entity import Entity


def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(40,25,"@",(255,255,255))
    npc = Entity(35,20,"g",(255,0,0))
    entities = {player,npc}
    engine = engine(entities,event_handler,player)

    with tcod.context.new_terminal(screen_width,screen_height,tileset=tileset,title="Lake",) as context:

        root_console = tcod.console.Console(screen_width, screen_height, order="F")

        while True:
            engine.render(root_console, context)
            events = tcod.event.wait()

            engine.handle_events(events)



if __name__ == "__main__":
    main()