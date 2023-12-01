import logging
import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from celery import Celery
import src.celery_settings


logging.basicConfig(level=logging.DEBUG)

iterations = 20

# MODEL_ID = "stabilityai/stable-diffusion-2-1-base"
MODEL_ID = "Yntec/epiCPhotoGasm"

class Managers:

    _logger = None
    _config = None
    _celery = None
    _stable_pipeline = None

    @property
    def logger(self):

        if self._logger is None:
            raise Exception('logger not initialized')

    # @property
    # def config(self):

    #     if self._config is None:
    #         raise Exception('config not initialized')

    @property
    def celery(self):

        if self._celery is None:
            raise Exception('celery not initialized')

    async def initialize(self):

        # logger
        self._logger = logging.getLogger()

        # celery
        self._celery = Celery()
        celery_app = Celery('tasks')
        celery_app.config_from_object(src.celery_settings)

        # stable diffusion
        _scheduler = EulerDiscreteScheduler.from_pretrained(MODEL_ID, subfolder="scheduler")
        self.stable_pipeline = StableDiffusionPipeline.from_pretrained(
            model_id, 
            scheduler=_scheduler, 
            torch_dtype=torch.float16
        )

    async def teardown(self):
        pass

# def generate_from_prompt(prompt, pipe, scheduler):
#     logging.debug('running')
#     prompt="banana"
#     logging.debug(f'running with pipe: {pipe}, prompt: {prompt}, iterations: {iterations}')
#     image = pipe(prompt, guidance_scale=9, num_inference_steps=iterations).images[0]
#     filename = f"output_1.jpg"
#     image.save(filename, 'JPEG', quality=70)
#     return True

managers = Managers()
