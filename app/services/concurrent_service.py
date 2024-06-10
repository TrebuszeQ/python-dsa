import concurrent.futures
import logging


class ConcurrencyFactory:
    @property
    def max_concurrent_workers(self):
        return self._max_concurrent_workers

    def __init__(self, config_dict):
        self._logger = logging.getLogger(self.__name__)
        self._config_dict = config_dict
        self._max_concurrent_workers = self._config_dict["MAX_EXECUTOR_WORKERS"]

    def concurrent_task(self, values_arr_list, callback):
        self._logger.info(f"Starting concurrent task: {callback.__name__}")

        futures = set()
        successful_dict = dict()
        not_successful = set()

        with concurrent.futures.ThreadPoolExecutor(max_workers=self._max_concurrent_workers) as executor:
            future_count = 0
            for value_arr in values_arr_list:
                self._logger.info(f"Submitting concurrent task no. {future_count} with values: {value_arr}")
                future = executor.submit(callback, value_arr)
                futures.add(future)
                future_count += 1

            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    successful_dict[f"{future}"] = result
                    self._logger.info(f"Concurrent task {callback.__name__} completed with result: {result}")
                except Exception as e:
                    not_successful.add(future)
                    self._logger.error(f"Future no. {future_count} failed with exception: {e}")

            self._logger.debug(f"Successful futures: {successful_dict}")
            self._logger.info(f"Successful futures count: {len(successful_dict)}")
            self._logger.debug(f"Not successful futures: {not_successful}")
            self._logger.info(f"Not successful futures count: {len(not_successful)}")
            return successful_dict