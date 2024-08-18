global data, isFetching
data = {}
isFetching = False


def use_query(key, query):
  i = 0
  status = 'error'
  res = query()
  while res is None:
    isFetching = True
    status = False
    i += 1
    if i == 3:
      status = 'error'
      isFetching = False
      break
  else:
    status = 'success'
    isFetching = False
    data.update({f"""{key}""": f"""{res}"""})
  return res, status


def use_mutation(key, mutation):
  res = data[f"""{key}"""]
  if res is not None:
    ret = mutation(res)
    res = ret
  else:
    isFetching = False
    return False


def isFetched():
  return isFetching
