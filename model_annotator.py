import os
import requests
import zipfile
import logging
import json
import Levenshtein
import pandas as pd
from markdown import markdown
from bs4 import BeautifulSoup


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename="model_annotation_logs.log",  # log output file
    filemode="a"
)


class ModelAnnotator:

    def __init__(
        self,
        url = "http://114.130.116.83/ml/ocr",
        src_dir=r"C:\Users\User\Downloads\TW_A",
        des_dir=r"C:\Users\User\Downloads\Output"
        
    ):
        self.url = url
        self.src_dir = src_dir
        self.des_dir = des_dir

        os.makedirs(des_dir, exist_ok=True)


    def get_response(self, file_name, force=False):

        zip_name = ".".join(file_name.split(".")[:-1]+["zip"])
        file_path = os.path.join(self.src_dir, file_name)
        zip_path = os.path.join(self.des_dir, zip_name)

        if not force and os.path.exists(zip_path):
            logging.info(f"Already exists: {zip_name}")
            return zip_name

        files = {"file": open(file_path, "rb")}
        data = {
            "prompt_mode": "prompt_layout_all_en",
            "bbox_x1": "0",
            "bbox_y1": "0",
            "bbox_x2": "0",
            "bbox_y2": "0",
            "fitz_preprocess": "true",
            "num_thread": "0"
        }

        response = requests.post(
            self.url,
            files=files,
            data=data,
            headers={"accept": "application/json"}
        )

        if response.status_code!=200:
            logging.info(f"Error: {response.text}")
            return None

        with open(zip_path, "wb") as f:
            f.write(response.content)

        return zip_name


    def main(self):

        for ct, fname in enumerate(sorted(os.listdir(self.src_dir))):
            logging.info(f"Processing foldera: {fname}")
            try:
                zip_fname = self.get_response(file_name=fname, force=False)
                logging.info("Response has been received from endpoint.")
                
            except Exception as e:
                logging.info(f"Error at {fname}: {e}")

            if ct==19:
                break


if __name__ == "__main__":

    logging.info("\n\n\n")
    ModelAnnotator().main()