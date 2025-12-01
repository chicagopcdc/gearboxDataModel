from sqlalchemy import Integer, String, DateTime, UniqueConstraint, ForeignKey, DECIMAL, Index
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy.sql import func

from .base_class import Base


class Site(Base):
    __tablename__ = "site"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String, nullable=True)
    country = mapped_column(String, nullable=True)
    city = mapped_column(String, nullable=True)
    state = mapped_column(String, nullable=True)
    zip = mapped_column(String, nullable=True)
    create_date = mapped_column(DateTime, nullable=True)
    source_id = mapped_column(
        Integer, ForeignKey("source.id", name="fk_site_source_id")
    )
    location_lat = mapped_column(DECIMAL(10, 8), nullable=True)
    location_long = mapped_column(DECIMAL(11, 8), nullable=True)

    # The following solution will work on postgres 15 or later
    # UniqueConstraint(name, location_lat, location_long, name="site_uix", postgresql_nulls_not_distinct=True)

    __table_args__ = (
        Index(
            'idx_name_lat_long',
            name,
            func.coalesce(location_lat, 0),
            func.coalesce(location_long, 0)
        ),
    )

    studies = relationship("SiteHasStudy", back_populates="site")
    site_source = relationship("Source", back_populates="sites", lazy="joined")
