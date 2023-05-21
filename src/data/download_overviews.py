from pathlib import Path

import fire
import numpy as np
import pandas as pd
import requests
from tqdm import tqdm

DATA_PATH = Path("data/")


def main(api_key: str):
    movie = pd.read_csv(DATA_PATH / "raw" / "links.csv")
    overview = []
    for tmb_id in tqdm(movie["tmdbId"].values):
        if np.isnan(tmb_id):
            overview.append("")
        else:
            url = f"https://api.themoviedb.org/3/movie/{int(tmb_id)}?api_key={api_key}&language=en-US"
            response = requests.get(url).json()
            overview.append(response.get("overview", ""))
    movie["overview"] = overview
    movie.to_csv(DATA_PATH / "external" / "movie_with_overview.csv", index=False)


if __name__ == "__main__":
    fire.Fire(main)
