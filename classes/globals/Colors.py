class Colors:
    # Basic Colors
    WHITE       = (1, 1, 1, 1)
    BLACK       = (0, 0, 0, 1)
    RED         = (1, 0, 0, 1)
    GREEN       = (0, 1, 0, 1)
    BLUE        = (0, 0, 1, 1)
    YELLOW      = (1, 1, 0, 1)
    CYAN        = (0, 1, 1, 1)
    MAGENTA     = (1, 0, 1, 1)
    GRAY        = (0.5, 0.5, 0.5, 1)
    TRANSPARENT = (0, 0, 0, 0)

    # Light Colors
    LIGHT_RED     = (1, 0.6, 0.6, 1)
    LIGHT_GREEN   = (0.6, 1, 0.6, 1)
    LIGHT_BLUE    = (0.6, 0.6, 1, 1)
    LIGHT_YELLOW  = (1, 1, 0.6, 1)
    LIGHT_CYAN    = (0.6, 1, 1, 1)
    LIGHT_MAGENTA = (1, 0.6, 1, 1)
    LIGHT_GRAY    = (0.75, 0.75, 0.75, 1)
    OFF_WHITE     = (0.95, 0.95, 0.95, 1)

    # Dark Colors
    DARK_RED     = (0.5, 0, 0, 1)
    DARK_GREEN   = (0, 0.5, 0, 1)
    DARK_BLUE    = (0, 0, 0.5, 1)
    DARK_YELLOW  = (0.5, 0.5, 0, 1)
    DARK_CYAN    = (0, 0.5, 0.5, 1)
    DARK_MAGENTA = (0.5, 0, 0.5, 1)
    DARK_GRAY    = (0.25, 0.25, 0.25, 1)

    # Earth Tones
    BROWN       = (0.6, 0.4, 0.2, 1)
    TAN         = (0.82, 0.71, 0.55, 1)
    OLIVE       = (0.5, 0.5, 0, 1)
    FOREST      = (0.13, 0.55, 0.13, 1)
    SAND        = (0.76, 0.7, 0.5, 1)
    CLAY        = (0.7, 0.4, 0.3, 1)
    SAGE        = (0.74, 0.78, 0.68, 1)

    # Pastel Colors
    PASTEL_PINK     = (1, 0.8, 0.86, 1)
    PASTEL_GREEN    = (0.7, 1, 0.7, 1)
    PASTEL_BLUE     = (0.7, 0.85, 1, 1)
    PASTEL_PURPLE   = (0.8, 0.7, 1, 1)
    PASTEL_YELLOW   = (1, 1, 0.7, 1)
    PASTEL_ORANGE   = (1, 0.85, 0.7, 1)
    PASTEL_MINT     = (0.7, 1, 0.9, 1)

    # Vibrant Colors
    ORANGE       = (1, 0.5, 0, 1)
    GOLD         = (1, 0.84, 0, 1)
    HOT_PINK     = (1, 0.41, 0.71, 1)
    LIME         = (0.75, 1, 0, 1)
    VIOLET       = (0.56, 0, 1, 1)
    INDIGO       = (0.29, 0, 0.51, 1)
    TURQUOISE    = (0.25, 0.88, 0.82, 1)

    # Utility Colors (UI/UX)
    SUCCESS      = (0.2, 0.8, 0.2, 1)
    WARNING      = (1, 0.65, 0, 1)
    ERROR        = (0.9, 0.1, 0.1, 1)
    INFO         = (0.1, 0.6, 0.9, 1)
    PRIMARY      = (0.1, 0.45, 0.85, 1)
    SECONDARY    = (0.6, 0.6, 0.6, 1)
    DISABLED     = (0.6, 0.6, 0.6, 0.5)

    # Named Variants (approx. HTML/CSS colors)
    MAROON       = (0.5, 0, 0, 1)
    NAVY         = (0, 0, 0.5, 1)
    CORAL        = (1, 0.5, 0.31, 1)
    SALMON       = (0.98, 0.5, 0.45, 1)
    CHOCOLATE    = (0.82, 0.41, 0.12, 1)
    TOMATO       = (1, 0.39, 0.28, 1)
    PLUM         = (0.87, 0.63, 0.87, 1)
    SKY_BLUE     = (0.53, 0.81, 0.92, 1)
    STEEL_BLUE   = (0.27, 0.51, 0.71, 1)
    MIDNIGHT     = (0.1, 0.1, 0.44, 1)
    SLATE        = (0.44, 0.5, 0.56, 1)
    LAVENDER     = (0.9, 0.9, 0.98, 1)
    SNOW         = (1, 0.98, 0.98, 1)
    SEASHELL     = (1, 0.96, 0.93, 1)
    IVORY        = (1, 1, 0.94, 1)
    HONEYDEW     = (0.94, 1, 0.94, 1)
    MINT_CREAM   = (0.96, 1, 0.98, 1)

    @classmethod
    def all(cls):
        """Return a dictionary of all defined colors."""
        return {
            k: v for k, v in cls.__dict__.items()
            if not k.startswith("__") and isinstance(v, tuple)
        }
