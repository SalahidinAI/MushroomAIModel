from mashroom.db.database import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Mushroom(Base):
    __tablename__ = 'mushroom'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    class_: Mapped[str] = mapped_column(String)
    cap_shape: Mapped[str] = mapped_column(String)
    cap_surface: Mapped[str] = mapped_column(String)
    cap_color: Mapped[str] = mapped_column(String)
    bruises: Mapped[str] = mapped_column(String)
    odor: Mapped[str] = mapped_column(String)
    gill_attachment: Mapped[str] = mapped_column(String)
    gill_spacing: Mapped[str] = mapped_column(String)
    gill_size: Mapped[str] = mapped_column(String)
    gill_color: Mapped[str] = mapped_column(String)
    stalk_shape: Mapped[str] = mapped_column(String)
    stalk_root: Mapped[str] = mapped_column(String)
    stalk_surface_above_ring: Mapped[str] = mapped_column(String)
    stalk_surface_below_ring: Mapped[str] = mapped_column(String)
    stalk_color_above_ring: Mapped[str] = mapped_column(String)
    stalk_color_below_ring: Mapped[str] = mapped_column(String)
    veil_type: Mapped[str] = mapped_column(String)
    veil_color: Mapped[str] = mapped_column(String)
    ring_number: Mapped[str] = mapped_column(String)
    ring_type: Mapped[str] = mapped_column(String)
    spore_print_color: Mapped[str] = mapped_column(String)
    population: Mapped[str] = mapped_column(String)
    habitat: Mapped[str] = mapped_column(String)
