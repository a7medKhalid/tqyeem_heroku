import json
from typing import final
from tqyeem_app.forms import CustomUserCreationForm
from tqyeem.settings import TIME_ZONE
from web3 import Web3
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# from .render import Render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
# from .forms import ProductForm, ApprovedSellerForm
from .models import ApprovedSeller

# ropsten acount
public_key = "0xb40f0AD8fb37EAa92f7115699B3Aca3bD00083bB"
private_key = "e771d18386c0e9797ff8b96cd4dd2bedd85863b379cae10812824f967c0054b5"

url = "https://ropsten.infura.io/v3/c5de5473f973490da5787ba871b51c40"

web3 = Web3(Web3.HTTPProvider(url))

address = web3.toChecksumAddress("0xc805FC02216Aa3Cf1826551D2fD59a8b973a68C6")
abi = json.loads('''[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "approved",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "ApprovalForAll",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "productID",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "reviewText",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "rating",
				"type": "uint256"
			}
		],
		"name": "addReview",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "tokenURI",
				"type": "string"
			}
		],
		"name": "createProduct",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "getApproved",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "productID",
				"type": "uint256"
			}
		],
		"name": "getReviews",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "reviews",
				"type": "string[]"
			},
			{
				"internalType": "uint256[]",
				"name": "ratings",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			}
		],
		"name": "isApprovedForAll",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "ownerOf",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			},
			{
				"internalType": "bytes",
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "setApprovalForAll",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes4",
				"name": "interfaceId",
				"type": "bytes4"
			}
		],
		"name": "supportsInterface",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "tokenURI",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')

contract = web3.eth.contract(address=address, abi=abi)

def add_review_to_product(productID,reviewText,rating):
    nonce = web3.eth.getTransactionCount('0xb40f0AD8fb37EAa92f7115699B3Aca3bD00083bB')

    tx = contract.functions.addReview(productID,reviewText,rating).buildTransaction({
        'chainId': 3,
        'gas': 3000000,
        'gasPrice': web3.toWei('40','gwei'),
        'nonce': nonce
    })

    signed_tx = web3.eth.account.signTransaction(tx,private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    count = 0 
    while tx_receipt is None and (count < 30):
        time.sleep(10)
        tx_receipt = web3.eth.getTransactionReceipt(result)

        print(tx_receipt)

def get_reviews_from_contract(productId):
    func = contract.functions["getReviews"]    
    reviews = func(productId).call()
    return reviews

def get_token_uri(productId):
	func = contract.functions["tokenURI"]
	uri = func(productId).call()
	return uri


# def get_user_products_from_contract(address):
	# use 





# views 

def test(request):
    reviews = get_reviews_from_contract(1)
    return HttpResponse(reviews)
# @login_required¬
def dashboard_view(request):


	return render(request,"dashboard.html")

def product_view(request, product_id):

	# get reveiws
	data = get_reviews_from_contract(product_id)
	reviews = data[0]
	ratings = data[1]
	finalData = []
	class reviewObject:
		def __init__(self, text, rating):
			self.text = text
			self.rating = rating
	
	for i in range(len(reviews)):
		x = reviewObject(reviews[i],ratings[i])

		finalData.append(x)



	# get uri
	uri = get_token_uri(product_id)

	# pass data to template
	args = {}
	args['finalData'] = finalData
	args['uri'] = uri
	args['productId'] = product_id



	# add review

	if request.method == 'POST':
		ratingText = request.POST.get('ratingText', "")
		rating = request.POST.get('rating', 3)
		add_review_to_product(product_id,ratingText,4)

		sellerName = request.POST.get('sellerName',"")
		sellerLink = request.POST.get('sellerLink',"")

		# product = Product(product_id)
		# product.save()
		seller = ApprovedSeller(productId=product_id,name=sellerName,url=sellerLink)
		seller.save()

	sellers = ApprovedSeller.objects.filter(productId=product_id)
	args['sellers'] = sellers
	
	return render(request, "singleProduct.html", args)

    






class signup_view(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'
