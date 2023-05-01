import pygame

screen = pygame.display.set_mode((1100, 650), pygame.NOFRAME)
clock = pygame.time.Clock()


def get_surrounding_area(width: int, screen: pygame.Surface) -> list[pygame.Rect]:
    screen_width, screen_height = screen.get_size()

    left_bar = pygame.Rect(0, 0, width, screen_height)
    right_bar = pygame.Rect(screen_width - width, 0, width, screen_height)
    top_bar = pygame.Rect(0, 0, screen_width, width)
    bottom_bar = pygame.Rect(0, screen_height - width, screen_width, width)
    return (left_bar, right_bar, top_bar, bottom_bar)


def get_drag(
    drag_offset: pygame.Vector2,
    original_mouse_pos: tuple,
    mouse_pos: tuple,
    diff: float,
) -> None:
    if pygame.mouse.get_pressed()[0]:
        drag_offset += (
            mouse_pos[0] - diff.x - original_mouse_pos[0],
            mouse_pos[1] - diff.y - original_mouse_pos[1],
        )
    else:
        drag_offset.x, drag_offset.y = 0, 0


surrounding_area = get_surrounding_area(30, screen)
first_resize = True
drag_offset = pygame.Vector2(0, 0)
mouse_pos = (0, 0)
original_size = screen.get_size()
original_mouse_pos = mouse_pos


while True:
    mouse_pos = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            raise SystemExit

    resizing = any(area.collidepoint(mouse_pos) for area in surrounding_area)
    if resizing:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)

        if first_resize:
            original_size = screen.get_size()
            original_mouse_pos = mouse_pos
            first_resize = False
        get_drag(
            drag_offset,
            original_mouse_pos,
            mouse_pos,
            screen.get_size() - pygame.Vector2(original_size),
        )
        pygame.display.set_mode(original_size + drag_offset, pygame.NOFRAME)
        surrounding_area = get_surrounding_area(30, screen)
    else:
        first_resize = True
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        first_resize = True
        drag_offset = pygame.Vector2(0, 0)

    # for area in surrounding_area:
    #     pygame.draw.rect(screen, "yellow", area)

    pygame.display.flip()
    clock.tick(60)
