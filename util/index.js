export function getArticles (page, perPage, articles) {
  const start = (page - 1) * perPage
  const end = start + perPage
  return articles.slice(start, end)
}

export function getPagerCount (totalCount, perCount) {
  let pagerCount = 0
  if (totalCount % perCount === 0) {
    pagerCount = totalCount / perCount
  } else {
    pagerCount = (totalCount - (totalCount % perCount)) / perCount + 1
  }
  return pagerCount
}

export function formatDate (date) {
  let year = new Date(date).getFullYear()
  let month = new Date(date).getMonth() + 1
  let day = new Date(date).getDate()
  month = month < 10 ? `0${month}` : month
  day = day < 10 ? `0${day}` : day
  return `${year}年${month}月${day}日`
}

export function formatArticles (articles, perCount) {
  let chunkResult = chunkArr(articles, perCount)
  let result = []
  for (let i = 0; i < chunkResult.length; i++) {
    // 抽离
    let datas = sortArr(chunkResult[i], 'date')
    // 根据所给数据结构进行赋值
    result.push([])
    for (let j = 0; j < datas.length; j++) {
      result[i].push({
        date: new Date(datas[j][0].date).getFullYear(),
        articles: []
      })
    }
    for (let k = 0; k < result[i].length; k++) {
      result[i][k].articles = sortArr(chunkResult[i], 'date')[k]
    }
  }
  return result[0]
}
function chunkArr (array, size) {
  // 获取数组的长度，如果你传入的不是数组，那么获取到的就是undefined
  const length = array.length
  // 判断不是数组，或者size没有设置，size小于1，就返回空数组
  if (!length || !size || size < 1) {
    return []
  }
  // 用来表示切割元素的范围start
  let index = 0
  // 用来递增表示输出数组的下标
  let resIndex = 0
  // 根据length和size算出输出数组的长度，并且创建它。
  let result = new Array(Math.ceil(length / size))
  // 进行循环
  while (index < length) {
    // 循环过程中设置result[0]和result[1]的值。该值根据array.slice切割得到。
    result[resIndex++] = array.slice(index, (index += size))
  }
  // 输出新数组
  // return result
  return result
}
function sortArr (array, prop) {
  let result = []
  let entry = []
  let temp = 0
  // 按照特定的参数将数组排序将具有相同值得排在一起
  array = array.sort((a, b) => {
    return a[prop] > b[prop] ? -1 : 1
  })
  if (array.length) {
    temp = new Date(array[0][prop]).getFullYear()
  }
  // 将相同类别的对象添加到统一个数组
  for (let i = 0; i < array.length; i++) {
    if (new Date(array[i][prop]).getFullYear() === temp) {
      entry.push(array[i])
    } else {
      temp = new Date(array[i][prop]).getFullYear()
      result.push(entry)
      entry = [array[i]]
    }
  }
  // 将最后的内容推出新数组
  result.push(entry)
  return result
}
