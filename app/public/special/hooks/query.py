import requests
from tenacity import RetryError, retry, stop_after_attempt, wait_fixed


class use_query:

  def __init__(self, query_key, query_fn, retry_attempts=3, wait_time=2):
    self.query_key = query_key
    self.query_fn = query_fn
    self.retry_attempts = retry_attempts
    self.wait_time = wait_time
    self.loading = True
    self.error = None
    self.data = None
    self._fetch_data()

  @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
  def _fetch_data(self):
    try:
      self.loading = True
      response = self.query_fn(self.query_key)
      response.raise_for_status()
      self.data = response.json()
      self.loading = False
    except RetryError as e:
      self.error = f"Request failed after {self.retry_attempts} retries: {e}"
      self.loading = False
    except requests.exceptions.RequestException as e:
      self.error = f"Request error: {e}"
      self.loading = False

  def get_data(self):
    return {"data": self.data, "loading": self.loading, "error": self.error}


class use_mutation:

  def __init__(self, mutation_fn, retry_attempts=3, wait_time=2):
    self.mutation_fn = mutation_fn
    self.retry_attempts = retry_attempts
    self.wait_time = wait_time
    self.loading = False
    self.error = None
    self.data = None

  @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
  def _mutate(self, *args, **kwargs):
    try:
      self.loading = True
      response = self.mutation_fn(*args, **kwargs)
      response.raise_for_status()
      self.data = response.json()
      self.loading = False
      return self.data
    except RetryError as e:
      self.error = f"Mutation failed after {self.retry_attempts} retries: {e}"
      self.loading = False
    except requests.exceptions.RequestException as e:
      self.error = f"Mutation error: {e}"
      self.loading = False

  def mutate(self, *args, **kwargs):
    self.error = None
    self.data = None
    return self._mutate(*args, **kwargs)

  def get_data(self):
    return {"data": self.data, "loading": self.loading, "error": self.error}
