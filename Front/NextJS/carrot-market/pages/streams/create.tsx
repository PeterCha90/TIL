import type { NextPage } from "next"

const Upload: NextPage = () => {
  return (
    <div className="space-y-5 px-4 py-16">
      <div className="my-5">
        <label
          className="mb-1  appearance-none w-full py-2 block  border-gray-300 rounded-md  shadow-sm placeholder-gray-400 focus:soutline-none focus:ring-orange-500 focus:border-orange-500"
          htmlFor="product_name"
        >
          Product Name
        </label>
        <div className="rounded-md relative shadow-sm flex items-center justify-center">
          <input
            className="appearance-none w-full pl-7 px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-orange-500 focus:border-orange-500"
            id="product_name"
            type="text"
            placeholder="0.00"
          />
        </div>
      </div>
      <div className="my-5">
        <label
          className="mb-1  appearance-none w-full py-2 block  border-gray-300 rounded-md  shadow-sm placeholder-gray-400 focus:soutline-none focus:ring-orange-500 focus:border-orange-500"
          htmlFor="price"
        >
          Price
        </label>
        <div className="rounded-md relative shadow-sm flex items-center justify-center">
          <div className="absolute flex items-center justify-center pointer-events-none left-0 pl-3 ">
            <span className="text-gray-500 text-sm">$</span>
          </div>
          <input
            className="appearance-none w-full pl-7 px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-orange-500 focus:border-orange-500"
            id="price"
            type="text"
            placeholder="0.00"
          />
          <div className="absolute right-0 pointer-events-none pr-3 flex items-center">
            <span className="text-gray-500 ">USD</span>
          </div>
        </div>
      </div>
      <div>
        <label className="mb-1 block appearance-none w-full  py-2  rounded-md rounded-l-none shadow-sm placeholder-gray-400 focus:soutline-none focus:ring-orange-500 focus:border-orange-500">
          Description
        </label>
        <textarea
          className="mt-1 shadow-sm w-full focus:ring-orange-500 rounded-md border-gray-300 focus:border-orange-500"
          rows={4}
        />
      </div>
      <button className="mt-5 w-full  bg-orange-500 hover:bg-orange-600 text-white py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium focus:ring-2  focus:ring-offset-2 focus:ring-orange-500 focus:outline-none">
        Go Live
      </button>
    </div>
  )
}

export default Upload
